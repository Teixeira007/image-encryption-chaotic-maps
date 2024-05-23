import cv2
import numpy as np
import matplotlib.pyplot as plt
import beach
import blocos_2
import function_f

imagem = cv2.imread('lena.png')

# image_cript, linhas, colunas = blocos_2.main(imagem)

# altura, largura = imagem.shape[:2]
# metade_altura = altura // 2
# metade_largura = largura // 2
left_block, right_block,  = blocos_2.dividir_em_blocos(imagem)

bloco_auxiliar_L = blocos_2.criar_bloco_auxiliar(right_block.shape, semente=45)
right_block  = blocos_2.xor_de_bloco(right_block, bloco_auxiliar_L)


left_block, linhas, colunas = function_f.main(left_block, 0.003, 0.983)
processed_image = np.hstack((right_block, left_block))


plt.imshow(processed_image)
plt.show()




left_block, right_block,  = blocos_2.dividir_em_blocos(processed_image)
left_block  = blocos_2.xor_de_bloco(left_block, bloco_auxiliar_L)

right_block = function_f.decript(right_block, 0.003, 0.983, linhas, colunas)
imagem_ = np.hstack((right_block, left_block))
# image_decript = blocos_2.decrypt(imagem, linhas, colunas)
plt.imshow(imagem_)
plt.show()



