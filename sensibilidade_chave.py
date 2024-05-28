import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt

def load_image(image_path):
    return cv2.imread(image_path, cv2.IMREAD_COLOR)

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def calculate_mse(imageA, imageB):
    # Mean Squared Error
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

def calculate_ssim(imageA, imageB):
    # Structural Similarity Index
    s, _ = ssim(imageA, imageB, full=True)
    return s


# Load images
image_path1 = 'imagens/sensibilidade_a_chave/img_cifrada_chave_0.001985_0.153972.bmp'
image_path2 = 'imagens/sensibilidade_a_chave/img_cifrada_chave_0.001986_0.153973.bmp'

image1 = load_image(image_path1)
image2 = load_image(image_path2)

# Convert to grayscale
gray_image1 = convert_to_grayscale(image1)
gray_image2 = convert_to_grayscale(image2)

# Calculate MSE
mse_value = calculate_mse(gray_image1, gray_image2)
print(f'Mean Squared Error (MSE): {mse_value}')

# Calculate SSIM
ssim_value = calculate_ssim(gray_image1, gray_image2)
print(f'Structural Similarity Index (SSIM): {ssim_value}')

