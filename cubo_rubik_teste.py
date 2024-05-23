import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
import beach


def iteracao_mapa_caotico(cubo, x, y, k):
    if x == 0:
        cubo = rotate_up(cubo, k)
    elif x == 1:
        cubo = rotate_down(cubo, k)
    elif x == 2:
        cubo = rotate_front(cubo, k)
    elif x == 3:
        cubo = rotate_back(cubo, k)
    elif x == 4:
        cubo = rotate_left(cubo, k)
    elif x == 5:
        cubo = rotate_right(cubo, k)
    
    if y == 0:
        cubo = rotate_up(cubo, k)
    elif y == 1:
        cubo = rotate_down(cubo, k)
    elif y == 2:
        cubo = rotate_front(cubo, k)
    elif y == 3:
        cubo = rotate_back(cubo, k)
    elif y == 4:
        cubo = rotate_left(cubo, k)
    elif y == 5:
        cubo = rotate_right(cubo, k)
    return cubo

def rotate_up(cubo, k):
    cubo[0] = np.rot90(cubo[0], k=k, axes=(1, 2))
    return cubo

def rotate_down(cubo, k):
    cubo[2] = np.rot90(cubo[2], k=k, axes=(1, 2))
    return cubo

def rotate_front(cubo, k):
   cubo[:, 2] = np.rot90(cubo[:, 2], k=k, axes=(1, 2))
   return cubo

def rotate_back(cubo, k):
    cubo[:, 0] = np.rot90(cubo[:, 0], k=k, axes=(1, 2))
    return cubo

def rotate_left(cubo, k):
    cubo[1, :, :, 0, :] = np.rot90(cubo[1, :, :, 0, :], k=k, axes=(2, 0))
    return cubo

def rotate_right(cubo, k):
    cubo[1, :, :, 2, :] = np.rot90(cubo[1, :, :, 2, :], k=k, axes=(2, 0))
    return cubo


def initialize_cubo_rubik(imagem):
    altura, largura, _ = imagem.shape
    largura_extra = 0
    altura_extra = 0

    if largura % 3 != 0 or altura % 3 != 0:
       imagem = redimensionar_para_divisibilidade_por_tres(imagem)
       altura, largura, _ = imagem.shape
       print(imagem.shape)
    
    altura_parte = imagem.shape[0] // 3
    largura_parte = imagem.shape[1] // 3
    # altura_extra = imagem.shape[0] - (altura_parte * 3)
    # largura_extra = imagem.shape[1] - (largura_parte * 3)

    # imagem = cv2.copyMakeBorder(imagem, 0, altura_extra, 0, largura_extra, cv2.BORDER_CONSTANT, value=(0, 0, 0))
    # altura_parte = imagem.shape[0] // 3
    # largura_parte = imagem.shape[1] // 3
    cubo_rubik = np.empty((3, 3, altura_parte, largura_parte, 3), dtype=np.uint8)

    # Preencher a matriz com as partes da imagem
    for i in range(3):
        for j in range(3):
            parte = imagem[i * altura_parte:(i + 1) * altura_parte, j * largura_parte:(j + 1) * largura_parte]
            cubo_rubik[i, j] = cv2.resize(parte, (largura_parte, altura_parte))
    
    return cubo_rubik, altura_extra, largura_extra

def permutacao_cubo_rubik(num_iteracoes, cubo, decript):
    if decript:
        x = beach.keygen_int(0.00542, 3.915, num_iteracoes) 
        y = beach.keygen_int(0.0847, 3.915, num_iteracoes)
        x.reverse()
        y.reverse()
        for i in range(num_iteracoes):
            cubo = iteracao_mapa_caotico(cubo, x[i], y[i], 1)
    else:
        x = beach.keygen_int(0.00542, 3.915, num_iteracoes) 
        y = beach.keygen_int(0.0847, 3.915, num_iteracoes)
        for i in range(num_iteracoes):
            cubo = iteracao_mapa_caotico(cubo, x[i], y[i], 3)
    return cubo

def redimensionar_para_divisibilidade_por_tres(imagem):
    altura, largura, _ = imagem.shape
    nova_altura = altura + (3 - altura % 3) % 3  # Redimensiona para uma altura divisível por 3
    nova_largura = largura + (3 - largura % 3) % 3  # Redimensiona para uma largura divisível por 3
    imagem_redimensionada = cv2.resize(imagem, (nova_largura, nova_altura))
    return imagem_redimensionada

def unir_partes(cubo):
    altura_parte, largura_parte = cubo.shape[2:4]
    altura_imagem = 3 * altura_parte
    largura_imagem = 3 * largura_parte
    imagem = np.zeros((altura_imagem, largura_imagem, 3), dtype=np.uint8)
    for i in range(3):
        for j in range(3):
            parte = cubo[i, j]
            imagem[i * altura_parte:(i + 1) * altura_parte, j * largura_parte:(j + 1) * largura_parte] = parte
    
    return imagem

def main(imagem):
    cubo_rubik, altura_extra, largura_extra = initialize_cubo_rubik(imagem)
    cubo = permutacao_cubo_rubik(50, cubo_rubik, False)
    imagem_re = unir_partes(cubo)
    # imagem_re = cv2.copyMakeBorder(imagem_re, 0, altura_extra, 0, largura_extra, cv2.BORDER_CONSTANT, value=(0, 0, 0))
    print(imagem_re.shape)
    plt.imshow(imagem_re)
    plt.title('baralhado')
    plt.show()

    # cubo_rubik_d, altura_extra_d, largura_extra_d = initialize_cubo_rubik(imagem_re)
    # # cubo_d = permutacao_cubo_rubik(100, cubo_rubik_d, True)
    # imagem_re_d = unir_partes(cubo_rubik_d)

    # imagem_final = remover_borda_extra(imagem_re_d, largura_extra, altura_extra)
    # imagem_re_d = cv2.copyMakeBorder(imagem_re_d, 0, altura_extra_d, 0, largura_extra_d, cv2.BORDER_CONSTANT, value=(0, 0, 0))
    
    # print(imagem_final.shape)

    # plt.imshow(imagem_re_d)
    # plt.title('desbaralhada')
    # plt.show()

    return imagem_re
   


if __name__ == "__main__":
    imagem = cv2.imread('lena.png')
    imagem_final = main(imagem)
    # plt.imshow(imagem_final)
    # plt.show()