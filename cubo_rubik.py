import cv2
import numpy as np
import random


def imagem_permutada(imagem, seed, seed_b):
 
    altura, largura, _ = imagem.shape

    random.seed(seed)
    linhas_permutadas = np.random.permutation(altura)
    random.seed(seed_b)  # Reinicia a semente para que as permutações de colunas sejam iguais às permutações de linhas
    colunas_permutadas = np.random.permutation(largura)

    # Salvar as permutações para posterior reversão
    linhas_permutadas_inversas = np.argsort(linhas_permutadas)
    colunas_permutadas_inversas = np.argsort(colunas_permutadas)

    # Aplicar as permutações na imagem
    imagem_permutada = np.zeros_like(imagem)
    for i in range(altura):
        for j in range(largura):
            imagem_permutada[i, j] = imagem[linhas_permutadas[i], colunas_permutadas[j]]

    return imagem_permutada, linhas_permutadas_inversas, colunas_permutadas_inversas


def decript(imagem_permutada, linhas_permutadas_inversas, colunas_permutadas_inversas):
    altura, largura, _ = imagem_permutada.shape
     # Voltar à imagem original
    imagem_original = np.zeros_like(imagem_permutada)
    for i in range(altura):
        for j in range(largura):
            imagem_original[i, j] = imagem_permutada[linhas_permutadas_inversas[i], colunas_permutadas_inversas[j]]

    return imagem_original

if __name__ == "__main__":
    imagem = cv2.imread('lena.png')
    permutada, linhas_permutadas_inversas, colunas_permutadas_inversas = imagem_permutada(imagem, 42, 231)
    cv2.imshow('Imagem Original', permutada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    original = decript(permutada, linhas_permutadas_inversas, colunas_permutadas_inversas)
    cv2.imshow('Imagem Original', original)
    cv2.waitKey(0)
    cv2.destroyAllWindows()