import cv2
import numpy as np
import matplotlib.pyplot as plt
import beach
import blocos_2
import function_f

imagem = cv2.imread('lena.png')

image_cript, linhas, colunas = blocos_2.main(imagem)
plt.imshow(image_cript)
plt.show()

image_decript = blocos_2.decrypt(image_cript, linhas, colunas)
plt.imshow(image_decript)
plt.show()





