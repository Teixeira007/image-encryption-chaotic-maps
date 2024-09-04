import cv2
import matplotlib.pyplot as plt
import blocos_2
import numpy as np

imagem = cv2.imread('imagens/imagens_para_teste/lena_gray_512.tif', cv2.IMREAD_GRAYSCALE)
# imagem = cv2.imread('modificada.bmp', cv2.IMREAD_GRAYSCALE)


# plt.imshow(imagem, cmap='gray')
# plt.show()

numbers = [0.0943063, 0.1987654, 0.7397466, 0.0098324, 0.0032313]

image_cript = blocos_2.main(imagem, numbers)
plt.imshow(image_cript, cmap=plt.cm.gray)
cv2.imwrite("lena_cifrado__.bmp" , image_cript)
plt.show()

numbers1 = [0.0943063, 0.1987654, 0.7397466, 0.0098324, 0.0032313]

image_decript = blocos_2.decrypt(image_cript, numbers1)
plt.imshow(image_decript, cmap=plt.cm.gray)
plt.show()

 

    

