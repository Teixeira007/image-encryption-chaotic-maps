import cv2
import numpy as np
import matplotlib.pyplot as plt
import beach
import cubo_rubik

def main(bloco, random_X, random_B, k5, k6):
    cubo = cubo_rubik.imagem_permutada(bloco, random_X, random_B)
    height = cubo.shape[0]
    width = cubo.shape[1]
    list_beach = beach.main(random_X, random_B, 10000)
    z=0
    enimg = np.zeros(shape=[height, width], dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            enimg[i, j] = cubo[i, j]^list_beach[z % len(list_beach)]
            z+=1

    enimg = cubo_rubik.imagem_permutada(enimg, k5, k6)
    return enimg


def  decript(imagem, random_X, random_B, linhas_permutadas_inversas, colunas_permutadas_inversas):
    imagem = cubo_rubik.decript(imagem, linhas_permutadas_inversas, colunas_permutadas_inversas)
    height = imagem.shape[0]
    width = imagem.shape[1]
    list_beach = beach.main(random_X, random_B, 10000)

    linhas_permutadas = beach.chaotic_permutation(height, random_X)
    colunas_permutadas = beach.chaotic_permutation(width, random_B)
  
    # Salvar as permutações para posterior reversão
    linhas_permutadas_inversas = np.argsort(linhas_permutadas)
    colunas_permutadas_inversas = np.argsort(colunas_permutadas)

    z=0
    decimg = np.zeros(shape=[height, width], dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            decimg[i, j] = imagem[i, j]^list_beach[z % len(list_beach)]
            z+=1
    
    imagem_final = cubo_rubik.decript(decimg, linhas_permutadas_inversas, colunas_permutadas_inversas)

    return imagem_final

if __name__ == "__main__":
    imagem = cv2.imread('imagens/imagens_para_teste/lena_gray_512.tif', cv2.IMREAD_GRAYSCALE)
    enigma =  main(imagem, 0.003, 0.983, 0.423423, 0.31321)
    plt.imshow(enigma)
    plt.show()
    linhas_permutadas = beach.chaotic_permutation(imagem.shape[0], 0.423423)
    colunas_permutadas = beach.chaotic_permutation(imagem.shape[0],  0.31321)
  
    # Salvar as permutações para posterior reversão
    linhas_permutadas_inversas = np.argsort(linhas_permutadas)
    colunas_permutadas_inversas = np.argsort(colunas_permutadas)
    imagem_ = decript(enigma, 0.003, 0.983, linhas_permutadas_inversas, colunas_permutadas_inversas)
    plt.imshow(imagem_)
    plt.show()




