import cv2
import matplotlib.pyplot as plt
import blocos_2

# Carregar a imagem em tons de cinza
imagem_cinza = cv2.imread('imagens/imagens_para_teste/lena_gray_512.tif', cv2.IMREAD_GRAYSCALE)

altered_image = imagem_cinza.copy()
altered_image[0,0] = (altered_image[0,0]+1)%256

numbers = [0.534234, 0.1987654, 0.23486, 0.973455, 0.563413]

image_cript = blocos_2.main(altered_image, numbers)
cv2.imwrite("lena_cifrado_1pixel__.bmp" , image_cript)

