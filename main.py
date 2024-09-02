import cv2
import matplotlib.pyplot as plt
import blocos_2
import numpy as np

imagem = cv2.imread('imagens/imagens_para_teste/lena_gray_512.tif', cv2.IMREAD_GRAYSCALE)
print(imagem.shape)
print("Forma da imagem:", imagem.shape)
print("Tipo da imagem:", imagem.dtype)
print("Valores máximos e mínimos:", np.min(imagem), np.max(imagem))
plt.imshow(imagem, cmap='gray')
plt.show()

numbers = [0.0943063, 0.1987654, 0.7397466, 0.0098324, 0.0032313]

image_cript = blocos_2.main(imagem, numbers)
plt.imshow(image_cript)
plt.imsave("lena_cifrado.bmp" , image_cript, cmap='gray')
plt.show()

numbers1 = [0.0943063, 0.1987654, 0.7397466, 0.0098324, 0.0032313]

image_decript = blocos_2.decrypt(image_cript, numbers1)
plt.imshow(image_decript, cmap='gray')
plt.show()

 

    

