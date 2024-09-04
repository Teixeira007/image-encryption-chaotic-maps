import random
from PIL import Image
import cv2
import numpy as np
from collections import Counter
import math
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def calculate_entropy(image):
    # Verifica se a imagem é colorida ou em tons de cinza
    if len(image.shape) == 3:
        # Imagem colorida
        channels = cv2.split(image)
        entropies = [calculate_entropy_single_channel(channel) for channel in channels]
        return np.mean(entropies)
    else:
        # Imagem em tons de cinza
        return calculate_entropy_single_channel(image)

def calculate_entropy_single_channel(channel):
    # Conta a frequência de cada valor de pixel no canal
    pixel_counts = Counter(channel.flatten())
    total_pixels = channel.size
    entropy = 0

    for count in pixel_counts.values():
        p_x = count / total_pixels
        entropy -= p_x * np.log2(p_x)
    
    return entropy

def plot_histogram(image_path, title):
    image = cv2.imread(image_path)  
    image_array = np.array(image)

    plt.figure(figsize=(4,4))
    plt.title(title)
    plt.xlabel('Valor do Pixel')
    plt.ylabel('Frequência')
    plt.hist(image_array.flatten(), bins=256, range=(0, 256), color='blue', alpha=0.7)
    plt.show()

def calculate_and_plot_correlation(original_image, encrypted_image):
    def correlation_coefficient(x, y):
        return np.corrcoef(x.flatten(), y.flatten())[0, 1]
    
    # Coeficientes de correlação em diferentes direções
    horizontal_corr = correlation_coefficient(original_image[:, :-1], original_image[:, 1:])
    vertical_corr = correlation_coefficient(original_image[:-1, :], original_image[1:, :])
    diagonal_corr = correlation_coefficient(original_image[:-1, :-1], original_image[1:, 1:])
    encrypted_horizontal_corr = correlation_coefficient(encrypted_image[:, :-1], encrypted_image[:, 1:])
    encrypted_vertical_corr = correlation_coefficient(encrypted_image[:-1, :], encrypted_image[1:, :])
    encrypted_diagonal_corr = correlation_coefficient(encrypted_image[:-1, :-1], encrypted_image[1:, 1:])

    print("Correlação imagem Lena")
    print("Horizontal:", horizontal_corr)
    print("Vertical:", vertical_corr)
    print("Diagonal:", diagonal_corr)

    print("Correlação imagem Lena Cifrada")
    print("Horizontal:", encrypted_horizontal_corr)
    print("Vertical:", encrypted_vertical_corr)
    print("Diagonal:", encrypted_diagonal_corr)

def correlacao_px_adjacente(image, height, width, title):
    samples_x = []
    samples_y = []
    
    for i in range(1024):
        x = random.randint(0, height - 2)
        y = random.randint(0, width - 1)
        
        # Verificar se estamos lidando com uma imagem em escala de cinza ou uma imagem colorida
        if len(image.shape) == 2:  # Imagem em escala de cinza
            samples_x.append(image[x, y])
            samples_y.append(image[x + 1, y])
        elif len(image.shape) == 3:  # Imagem colorida
            # Se for uma imagem colorida, escolha um canal (por exemplo, canal R)
            samples_x.append(image[x, y, 0])
            samples_y.append(image[x + 1, y, 0])
        else:
            raise ValueError("Formato de imagem não suportado")
    
    # Converter listas para arrays numpy unidimensionais
    samples_x = np.array(samples_x).flatten()
    samples_y = np.array(samples_y).flatten()
    
    # Calcular a correlação de Pearson
    correlation, _ = pearsonr(samples_x, samples_y)
    
    # Visualização
    plt.figure(figsize=(5, 5))
    plt.scatter(samples_x, samples_y, s=2)
    plt.title(f'{title}\nCorrelação: {correlation:.4f}')
    plt.xlabel('Pixel (x, y)')
    plt.ylabel('Pixel (x+1, y)')
    plt.show()
    
    return correlation
def calculate_entropy(image):
    histogram = Counter(image.flatten())
    total_pixels = image.size
    entropy = 0
    for count in histogram.values():
        p = count / total_pixels
        entropy -= p * np.log2(p)
    return entropy
# Exemplo de uso:
# Carregar a imagem cifrada (supondo que 'imagem_cifrada' é um array numpy)
imagem_cifrada = cv2.imread('lena_cifrado__.bmp',0)
print(imagem_cifrada.shape)
image = cv2.imread("imagens/imagens_para_teste/lena_gray_512.tif",0)

# Calcular a entropia
# entropy = calculate_entropy(imagem_cifrada)
entropy = calculate_entropy(imagem_cifrada)
print(f"Entropia da imagem cifrada: {entropy}")


max_entropy = 8  # Máxima entropia para uma imagem de 8 bits
print(f"Entropy of the encrypted image: {entropy:.4f} bits per pixel")
print(f"Maximum possible entropy: {max_entropy} bits per pixel")
print(f"Entropy percentage: {(entropy / max_entropy) * 100:.2f}%")

plot_histogram("imagens/imagens_para_teste/lena_gray_512.tif", 'Histograma da Imagem Original')
plot_histogram("lena_cifrado__.bmp", 'Histograma da Imagem Criptografada')


original_image = np.array(image)


encrypted_image = np.array(imagem_cifrada)
calculate_and_plot_correlation(original_image,encrypted_image)

height, width = image.shape
correlacao_px_adjacente(original_image, height, width, "Correlação dos Pixels Adjacente- Imagem Original")
correlacao_px_adjacente(encrypted_image, height, width, "Correlação dos Pixels Adjacente - Imagem Cifrada")

