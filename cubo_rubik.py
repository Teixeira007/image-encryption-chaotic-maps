import cv2
import numpy as np
import random
import beach


def imagem_permutada(imagem, seed, seed_b):
 
    altura, largura= imagem.shape
    linhas_permutadas = beach.chaotic_permutation(altura, seed)
    colunas_permutadas = beach.chaotic_permutation(largura, seed_b)
    imagem_permutada_ = np.zeros_like(imagem)
    
    #Aplicar as permutações na imagem
    for i in range(altura):
        for j in range(largura):
            imagem_permutada_[i, j] = imagem[linhas_permutadas[i], colunas_permutadas[j]]

    return imagem_permutada_


def decript(imagem_permutada, linhas_permutadas_inversas, colunas_permutadas_inversas):
    altura, largura = imagem_permutada.shape
    #Voltar à imagem original
    imagem_original = np.zeros_like(imagem_permutada)
    for i in range(altura):
        for j in range(largura):
            imagem_original[i, j] = imagem_permutada[linhas_permutadas_inversas[i], colunas_permutadas_inversas[j]]

    return imagem_original


if __name__ == "__main__":
    imagem = cv2.imread('imagens/imagens_para_teste/lena_gray_512.tif', cv2.IMREAD_GRAYSCALE)
    height, width = imagem.shape
    linhas_permutadas = beach.chaotic_permutation(height, 0.42342334)
    colunas_permutadas = beach.chaotic_permutation(width, 0.942344)
    linhas_permutadas_inversas = np.argsort(linhas_permutadas)
    colunas_permutadas_inversas = np.argsort(colunas_permutadas)
    permutada = imagem_permutada(imagem, 0.42342334, 0.942344)
    cv2.imshow('Imagem Original', permutada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    original = decript(permutada, linhas_permutadas_inversas, colunas_permutadas_inversas)
    cv2.imshow('Imagem', original)
    cv2.waitKey(0)
    cv2.destroyAllWindows()