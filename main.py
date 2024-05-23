import cv2
import numpy as np
import matplotlib.pyplot as plt
import beach
import blocos_2
import function_f
import key as k

imagem = cv2.imread('lena.png')

key, key__ = k.encrypt_numbers()
image_cript, linhas, colunas = blocos_2.main(imagem, key, key__)
plt.imshow(image_cript)
plt.show()

image_decript = blocos_2.decrypt(image_cript, linhas, colunas, key, key__)
plt.imshow(image_decript)
plt.show()





