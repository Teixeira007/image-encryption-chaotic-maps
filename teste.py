import cv2
import matplotlib.pyplot as plt


# Carregar a imagem em tons de cinza
imagem_cinza = cv2.imread('imagens/imagens_para_teste/lena_cifrado.bmp')

# Definir as coordenadas do pixel a ser alterado
x, y = 50, 100  # Exemplo de coordenadas

# Alterar o valor do pixel
imagem_cinza[y, x] = 200  # Novo valor do pixel (entre 0 e 255)

# Salvar ou exibir a imagem modificada
plt.imsave("modificada.bmp", imagem_cinza)
