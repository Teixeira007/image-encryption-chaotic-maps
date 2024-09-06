import cv2
import matplotlib.pyplot as plt
import blocos_2
import numpy as np

imagem = cv2.imread('imagens/imagens_para_teste/lena_gray_512.tif', cv2.IMREAD_GRAYSCALE)

numbers = [0.534234, 0.1987654, 0.23486, 0.973455, 0.563413]

image_cript = blocos_2.main(imagem, numbers)
plt.imshow(image_cript, cmap=plt.cm.gray)
cv2.imwrite("lena_cifrado.bmp" , image_cript)
plt.show()

numbers1 = [0.534234, 0.1987654, 0.23486, 0.973455, 0.563413]

image_decript = blocos_2.decrypt(image_cript, numbers1)
plt.imshow(image_decript, cmap=plt.cm.gray)
plt.show()

 

    

