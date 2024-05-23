import cv2
import numpy as np
import matplotlib.pyplot as plt
import function_f
import random
import beach

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
    # height, width, channels = image.shape

    # # Create XOR array with the same shape as the right block
    # xor_array = np.random.randint(0, 256, (height, width // 2, channels), dtype=np.uint8)
    # Criar um bloco auxiliar com dimensão especificada
    bloco_auxiliar = np.random.randint(0, 256, size=dimensao, dtype=np.uint8)  # Valores aleatórios entre 0 e 255
    return bloco_auxiliar


def xor_de_bloco(bloco, bloco_auxiliar):
    # Aplicar a operação XOR entre o bloco original e o bloco auxiliar
    resultado_xor = np.bitwise_xor(bloco, bloco_auxiliar)
    return resultado_xor


def l_r(right_block, left_block, aux, random_numbers_X, random_numbers_B):
            right_block = xor_de_bloco(right_block, aux)
            left_block = xor_de_bloco(left_block, bloco_teste)
            # left_block = function_f.main(left_block, random_numbers_X, random_numbers_B)
            processed_image = np.hstack((right_block, left_block))
            return processed_image

bloco_teste = criar_bloco_auxiliar((512,256,3), semente=43234)

def main(imagem):# Carregar a imagem
    # Dividir a imagem em blocos
    left_block, right_block,  = dividir_em_blocos(imagem)

    dimensao = left_block.shape

    semente = 42

    random_numbers_X = beach.keygen(000.1, 3.915, 7)

    random_numbers_B = beach.keygen(00.153, 3.915, 7)

    bloco_auxiliar_L = criar_bloco_auxiliar(dimensao, semente=semente)

    
    for i in range (3):
        l_next = l_r(left_block, right_block, bloco_auxiliar_L, random_numbers_X[i], random_numbers_B[i])



    return l_next
        

def decrypt(imagem):
    height, width, channels = imagem.shape
    mid = width // 2
    left_block = imagem[:, :mid, :]
    right_block = imagem[:, mid:, :]

    dimensao = left_block.shape

    semente = 42

    random_numbers_X = beach.keygen(000.1, 3.915, 7)

    random_numbers_B = beach.keygen(00.153, 3.915, 7)

    bloco_auxiliar_L = criar_bloco_auxiliar(dimensao, semente=semente)

    # Inverter a ordem das chaves para decriptação
    random_numbers_X = random_numbers_X[::-1]
    random_numbers_B = random_numbers_B[::-1]

    for i in range(3):
        l_next = l_r(left_block, right_block, bloco_auxiliar_L, random_numbers_X[i], random_numbers_B[i])

    return l_next

if __name__ == "__main__":
    imagem = cv2.imread('lena.png')
    image_ = main(imagem)

    
    plt.imshow(image_)
    plt.show()

    image__ = decrypt(image_)
    plt.imshow(image__)
    plt.show()



