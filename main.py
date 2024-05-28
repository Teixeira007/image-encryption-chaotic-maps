import cv2
import matplotlib.pyplot as plt
import blocos_2
import key as k

imagem = cv2.imread('lena.png')
plt.show()

key, key__ = k.encrypt_numbers()
image_cript, linhas, colunas = blocos_2.main(imagem, key, key__)
plt.imshow(image_cript)
plt.imsave("img_cifrada_chave_0.1987_0.73974_76453454.0_534675657.0.bmp", image_cript, cmap='gray')
plt.show()

image_decript = blocos_2.decrypt(image_cript, linhas, colunas, key, key__)
plt.imshow(image_decript)
plt.show()

 

    

