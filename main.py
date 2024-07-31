import cv2
import matplotlib.pyplot as plt
import blocos_2

imagem = cv2.imread('imagens/imagens_para_teste/lena_gray_512.tif')
plt.show()

numbers = [0.0943063, 0.1987654, 0.7397466, 0.0098324, 0.0032313]

image_cript = blocos_2.main(imagem, numbers)
plt.imshow(image_cript)
plt.imsave("lena_cifrado.bmp", image_cript, cmap='gray')
plt.show()

numbers1 = [0.0943063, 0.1987654, 0.7397466, 0.0098324, 0.0032313]

image_decript = blocos_2.decrypt(image_cript, numbers1)
plt.imshow(image_decript)
plt.show()

 

    

