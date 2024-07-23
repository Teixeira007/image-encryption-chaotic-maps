import cv2
import matplotlib.pyplot as plt
import blocos_2
import key as k

imagem = cv2.imread('lena.png')
plt.show()

numbers = [6534234.0, 0.1987, 4.0, 0.73974, 4.0, 76453454.0, 534675657.0]

key, key__ = k.encrypt_numbers()
image_cript, linhas, colunas = blocos_2.main(imagem, numbers)
plt.imshow(image_cript)
plt.imsave("img_cifrada_chave_1.bmp", image_cript, cmap='gray')
plt.show()

numbers1 = [65342341.0, 0.1987, 4.0, 0.73974, 4.0, 76453454.0, 534675657.0]

image_decript = blocos_2.decrypt(image_cript, linhas, colunas, numbers1)
plt.imshow(image_decript)
plt.show()

 

    

