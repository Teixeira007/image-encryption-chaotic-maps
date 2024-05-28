import random
from PIL import Image
import cv2
import numpy as np
from collections import Counter
import math
import matplotlib.pyplot as plt


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

# Exemplo de uso:
# Carregar a imagem cifrada (supondo que 'imagem_cifrada' é um array numpy)
imagem_cifrada = cv2.imread('img_cifrada_chave_0.1987_0.73974_76453454.0_534675657.0.bmp')

# Calcular a entropia
entropy = calculate_entropy(imagem_cifrada)
print(f"Entropia da imagem cifrada: {entropy}")


def plot_histogram(image_path, title):
    image = cv2.imread(image_path)  # Converter para escala de cinza
    image_array = np.array(image)

    plt.figure()
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
        x = random.randint(0,height-2)
        y = random.randint(0,width-1)
        samples_x.append(image[x][y])
        samples_y.append(image[x+1][y])
    plt.figure(figsize=(6,4))
    plt.scatter(samples_x,samples_y,s=2)
    plt.title(title)
    plt.show()

# Exemplo de uso:
image = cv2.imread("imagens/lena.bmp")
encrypted_image_path = 'img_cifrada_chave_0.1987_0.73974_76453454.0_534675657.0.bmp'
# entropy = calculate_entropy(encrypted_image_path)

max_entropy = 8  # Máxima entropia para uma imagem de 8 bits
print(f"Entropy of the encrypted image: {entropy:.4f} bits per pixel")
print(f"Maximum possible entropy: {max_entropy} bits per pixel")
print(f"Entropy percentage: {(entropy / max_entropy) * 100:.2f}%")

plot_histogram("imagens/lena.bmp", 'Histograma da Imagem Original')
plot_histogram(encrypted_image_path, 'Histograma da Imagem Criptografada')


original_image = np.array(image)
image_2 = cv2.imread(encrypted_image_path)

encrypted_image = np.array(image_2)
calculate_and_plot_correlation(original_image,encrypted_image)

height, width, _ = image.shape
correlacao_px_adjacente(original_image, height, width, "Adjacent Pixel Autocorrelation - Original Image")
correlacao_px_adjacente(encrypted_image, height, width, "Adjacent Pixel Autocorrelation - Original Encrypted")

