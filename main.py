import cv2
import matplotlib.pyplot as plt
import blocos_2
import key as k

imagem = cv2.imread('lena.png')
plt.show()

key, key__ = k.encrypt_numbers()
image_cript, linhas, colunas = blocos_2.main(imagem, key, key__)
plt.imshow(image_cript)
plt.imsave("img_cifrada_chave_totalmente_diferente.bmp", image_cript, cmap='gray')
plt.show()

image_decript = blocos_2.decrypt(image_cript, linhas, colunas, key, key__)
plt.imshow(image_decript)
plt.show()





