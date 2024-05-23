import cv2
import numpy as np
import matplotlib.pyplot as plt
import beach
import blocos_2

imagem = cv2.imread('lena.png')

image_cript, linhas, colunas = blocos_2.main(imagem)

altura, largura = imagem.shape[:2]
metade_altura = altura // 2
metade_largura = largura // 2

# imagem_final = np.zeros(shape=[altura, largura, 3], dtype=np.uint8)

# Definir as posições para cada bloco na imagem final
# Supondo que os blocos foram divididos na ordem: bloco1, bloco2, bloco3, bloco4
# Você precisa ajustar essas posições de acordo com a sua lógica de divisão de blocos
# imagem_final[0:metade_altura, 0:metade_largura] = l1
# imagem_final[0:metade_altura, metade_largura:] = l2
# imagem_final[metade_altura:, 0:metade_largura] = r1
# imagem_final[metade_altura:, metade_largura:] = r2


plt.imshow(image_cript)
plt.show()

image_decript = blocos_2.decrypt(imagem, linhas, colunas)
plt.imshow(image_decript)
plt.show()

