import cv2
import matplotlib.pyplot as plt
import blocos_2

imagem = cv2.imread('lena.png')
plt.show()

numbers = [65342341.0, 0.1987, 0.73974, 0.0098324, 0.0032313]

image_cript = blocos_2.main(imagem, numbers)
plt.imshow(image_cript)
plt.imsave("img_cifrada_chave_1.bmp", image_cript, cmap='gray')
plt.show()

numbers1 = [65342341.0, 0.1987, 0.73974, 0.0098324, 0.0032313]

image_decript = blocos_2.decrypt(image_cript, numbers1)
plt.imshow(image_decript)
plt.show()

 

    

