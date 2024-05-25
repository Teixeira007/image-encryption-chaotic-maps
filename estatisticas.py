from PIL import Image
import cv2
import numpy as np
from collections import Counter
import math
import matplotlib.pyplot as plt


def calculate_entropy(image_path):
    with Image.open(image_path) as img:
        # Convert image to grayscale if it's not already
        img = img.convert('L')
        pixels = np.array(img).flatten()
    
    histogram = Counter(pixels)
    total_pixels = len(pixels)
    
    entropy = 0
    for pixel_value in histogram:
        probability = histogram[pixel_value] / total_pixels
        entropy -= probability * math.log2(probability)
    
    return entropy

# Exemplo de uso:
encrypted_image_path = 'imagens/lena_cifrada.bmp'
entropy = calculate_entropy(encrypted_image_path)
max_entropy = 8  # Máxima entropia para uma imagem de 8 bits
print(f"Entropy of the encrypted image: {entropy:.4f} bits per pixel")
print(f"Maximum possible entropy: {max_entropy} bits per pixel")
print(f"Entropy percentage: {(entropy / max_entropy) * 100:.2f}%")

def plot_histogram(image_path, title):
    image = Image.open(image_path)  # Converter para escala de cinza
    image_array = np.array(image)

    plt.figure()
    plt.title(title)
    plt.xlabel('Valor do Pixel')
    plt.ylabel('Frequência')
    plt.hist(image_array.flatten(), bins=256, range=(0, 256), color='blue', alpha=0.7)
    plt.show()

plot_histogram("imagens/lena.bmp", 'Histograma da Imagem Original')
plot_histogram("imagens/lena_cifrada.bmp", 'Histograma da Imagem Criptografada')

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



image = Image.open("imagens/lena.bmp")  # Converter para escala de cinza
original_image = np.array(image)

image_2 = Image.open("imagens/img_cifrada_r_3.99.bmp")  # Converter para escala de cinza
encrypted_image = np.array(image_2)
calculate_and_plot_correlation(original_image,encrypted_image)

