import cv2
import numpy as np
import matplotlib.pyplot as plt
import function_f
import random
import beach
import key as k

def dividir_em_blocos(imagem):
    # Determinar as dimensões da imagem
    altura, largura = imagem.shape[:2]
    
    # Calcular as dimensões dos blocos
    metade_largura = largura // 2
    
    # Se a altura ou largura não forem divisíveis por 2, ajustar para que seja
    if altura % 2 != 0:
        altura -= 1
    if largura % 2 != 0:
        largura -= 1
    
    # Dividir a imagem em 2 blocos
    left_block = imagem[:, :metade_largura]
    right_block = imagem[:, metade_largura:]
    
    return left_block, right_block

def criar_bloco_auxiliar(dimensao, semente):
    # Definir a semente para a geração de números aleatórios
    np.random.seed(semente)
    bloco_auxiliar = np.random.randint(0, 256, size=dimensao, dtype=np.uint8)  # Valores aleatórios entre 0 e 255
    return bloco_auxiliar


def xor_de_bloco(bloco, bloco_auxiliar):
    # Aplicar a operação XOR entre o bloco original e o bloco auxiliar
    resultado_xor = np.bitwise_xor(bloco, bloco_auxiliar)
    return resultado_xor


def l_r(left_block, right_block, aux, random_numbers_X, random_numbers_B, lista_linhas, lista_colunas, k5, k6):
    right_block = xor_de_bloco(right_block, aux)
    left_block, linhas, colunas = function_f.main(left_block, random_numbers_X, random_numbers_B, k5, k6)
    lista_linhas.append(linhas)
    lista_colunas.append(colunas)
    processed_image = np.hstack((right_block, left_block))
    return processed_image, lista_linhas, lista_colunas

def l_r_reverse(left_block, right_block, aux, random_numbers_X, random_numbers_B, linhas, colunas):
    left_block  = xor_de_bloco(left_block, aux)
    right_block = function_f.decript(right_block, random_numbers_X, random_numbers_B, linhas, colunas)
    processed_image = np.hstack((right_block, left_block))
    return processed_image


def main(imagem, key, key__):

    key = k.decrypt_numbers(key, key__)
    # Dividir a imagem em blocos
    left_block, right_block  = dividir_em_blocos(imagem)
    dimensao = left_block.shape

    semente = int(key[0])
    l_next = imagem
    random_numbers_X = beach.keygen(key[1], key[2], 7)

    random_numbers_B = beach.keygen(key[3], key[4], 7)

    bloco_auxiliar_L = criar_bloco_auxiliar(dimensao, semente=semente)
    lista_linhas = []
    lista_colunas = []
    
    for i in range (7):
        left_block, right_block  = dividir_em_blocos(l_next)
        l_next, linhas, colunas = l_r(left_block, right_block, bloco_auxiliar_L, random_numbers_X[i], random_numbers_B[i], lista_linhas, lista_colunas, key[5], key[6])

    return l_next, linhas, colunas
        

def decrypt(imagem, lista_linhas, lista_colunas, key, key__):
    key = k.decrypt_numbers(key, key__)

    height, width, channels = imagem.shape
    mid = width // 2
    left_block = imagem[:, :mid, :]
    right_block = imagem[:, mid:, :]

    dimensao = left_block.shape

    semente = int(key[0])

    random_numbers_X = beach.keygen(key[1], key[2], 7)

    random_numbers_B = beach.keygen(key[3], key[4], 7)

    bloco_auxiliar_L = criar_bloco_auxiliar(dimensao, semente=semente)
    l_next = imagem
    # Inverter a ordem das chaves para decriptação
    random_numbers_X = random_numbers_X[::-1]
    random_numbers_B = random_numbers_B[::-1]

    lista_linhas = lista_linhas[::-1]
    lista_colunas = lista_colunas[::-1]

    for i in range(7):
        left_block, right_block  = dividir_em_blocos(l_next)
        l_next = l_r_reverse(left_block, right_block, bloco_auxiliar_L, random_numbers_X[i], random_numbers_B[i], lista_linhas[i], lista_colunas[i])

    return l_next

if __name__ == "__main__":
    imagem = cv2.imread('lena.png')
    image_, linhas, colunas = main(imagem)
    plt.imshow(image_)
    plt.show()
    image__ = decrypt(image_, linhas, colunas)
    plt.imshow(image__)
    plt.show()



