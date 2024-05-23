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
    metade_altura = altura // 2
    metade_largura = largura // 2
    
    # Se a altura ou largura não forem divisíveis por 2, ajustar para que seja
    if altura % 2 != 0:
        altura -= 1
    if largura % 2 != 0:
        largura -= 1
    
    # Dividir a imagem em 4 blocos
    bloco1 = imagem[0:metade_altura, 0:metade_largura]
    bloco2 = imagem[0:metade_altura, metade_largura:]
    bloco3 = imagem[metade_altura:, 0:metade_largura]
    bloco4 = imagem[metade_altura:, metade_largura:]
    
    return bloco1, bloco2, bloco3, bloco4

def criar_bloco_auxiliar(dimensao, semente):
    # Definir a semente para a geração de números aleatórios
    np.random.seed(semente)
    
    # Criar um bloco auxiliar com dimensão especificada
    bloco_auxiliar = np.random.randint(0, 256, size=dimensao, dtype=np.uint8)  # Valores aleatórios entre 0 e 255
    return bloco_auxiliar


def xor_de_bloco(bloco, bloco_auxiliar):
    # Aplicar a operação XOR entre o bloco original e o bloco auxiliar
    resultado_xor = np.bitwise_xor(bloco, bloco_auxiliar)
    return resultado_xor


def l_r(bloco_1, bloco_2, aux, random_numbers_X, random_numbers_B):
            xor_1 = xor_de_bloco(bloco_1, aux)
            f2 = xor_de_bloco(bloco_2, bloco_teste)
            # f2 = function_f.main(bloco_2, random_numbers_X, random_numbers_B)
            xor_f2 = xor_de_bloco(f2, aux)
            result_xor = xor_de_bloco(xor_f2, xor_1)
            return result_xor

bloco_teste = criar_bloco_auxiliar((256,256,3), semente=43234)

def main(imagem):# Carregar a imagem
    # Dividir a imagem em blocos
    bloco_l1, bloco_l0, bloco_r1, bloco_r0 = dividir_em_blocos(imagem)

    dimensao = bloco_l1.shape
    dimensaoR = bloco_r1.shape

    semente = 42
    sementeR = 76
    seed = 12095
    seed_B = 93723

    random_numbers_X = beach.keygen(000.1, 3.915, 7)

    random_numbers_B = beach.keygen(00.153, 3.915, 7)

    bloco_auxiliar_L = criar_bloco_auxiliar(dimensao, semente=semente)
    bloco_auxiliar_R = criar_bloco_auxiliar(dimensaoR, semente=sementeR)
    
    
    for i in range (3):
        l_next = l_r(bloco_l1, bloco_l0, bloco_auxiliar_L, random_numbers_X[i], random_numbers_B[i])
        r_next = l_r(bloco_r1, bloco_r0, bloco_auxiliar_R, random_numbers_X[i], random_numbers_B[i])

        aux_r = bloco_r0
        aux_l = bloco_l0

        bloco_l0 = l_next
        bloco_r0 = r_next

        bloco_l1 = aux_r
        bloco_r1 = aux_l


    return bloco_l1, bloco_l0, bloco_r1, bloco_r0
        
def l_r_inverse(bloco_1, bloco_2, aux, random_numbers_X, random_numbers_B):
    xor_f2 = xor_de_bloco(bloco_2, aux)
    f2 = xor_de_bloco(xor_f2, bloco_teste)
    # f2 = function_f.main(xor_f2, random_numbers_X, random_numbers_B)
    result_xor = xor_de_bloco(bloco_1, f2)
    xor_1 = xor_de_bloco(result_xor, aux)
    return xor_1

def decrypt(imagem):
    bloco_l1, bloco_l0, bloco_r1, bloco_r0 = dividir_em_blocos(imagem)

    dimensao = bloco_l1.shape
    dimensaoR = bloco_r1.shape

    semente = 42
    sementeR = 76
    seed = 12095
    seed_B = 93723

    random_numbers_X = beach.keygen(000.1, 3.915, 7)

    random_numbers_B = beach.keygen(00.153, 3.915, 7)

    bloco_auxiliar_L = criar_bloco_auxiliar(dimensao, semente=semente)
    bloco_auxiliar_R = criar_bloco_auxiliar(dimensaoR, semente=sementeR)

    # Inverter a ordem das chaves para decriptação
    random_numbers_X = random_numbers_X[::-1]
    random_numbers_B = random_numbers_B[::-1]

    for i in range(3):
        aux_r = bloco_r0
        aux_l = bloco_l0

        l_next = l_r_inverse(bloco_l1, bloco_l0, bloco_auxiliar_L, random_numbers_X[i], random_numbers_B[i])
        r_next = l_r_inverse(bloco_r1, bloco_r0, bloco_auxiliar_R, random_numbers_X[i], random_numbers_B[i])

        bloco_l0 = aux_l
        bloco_r0 = aux_r

        bloco_l1 = l_next
        bloco_r1 = r_next

    return bloco_l1, bloco_l0, bloco_r1, bloco_r0

if __name__ == "__main__":
    imagem = cv2.imread('lena.png')
    l1, l2, r1, r2 = main(imagem)

    altura, largura = imagem.shape[:2]
    metade_altura = altura // 2
    metade_largura = largura // 2

    imagem_final = np.zeros(shape=[altura, largura, 3], dtype=np.uint8)
    imagem_final[0:metade_altura, 0:metade_largura] = l1
    imagem_final[0:metade_altura, metade_largura:] = l2
    imagem_final[metade_altura:, 0:metade_largura] = r1
    imagem_final[metade_altura:, metade_largura:] = r2
    plt.imshow(imagem_final)
    plt.show()
    l1_, l2_, r1_, r2_  = decrypt(imagem_final)
    imagem_final_ = np.zeros(shape=[altura, largura, 3], dtype=np.uint8)
    imagem_final_[0:metade_altura, 0:metade_largura] = l1_
    imagem_final_[0:metade_altura, metade_largura:] = l2_
    imagem_final_[metade_altura:, 0:metade_largura] = r1_
    imagem_final_[metade_altura:, metade_largura:] = r2_
    plt.imshow(imagem_final_)
    plt.show()



