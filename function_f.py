import cv2
import numpy as np
import matplotlib.pyplot as plt
import beach
import cubo_rubik

def main(bloco, random_X, random_B, k5, k6):
    height = bloco.shape[0]
    width = bloco.shape[1]
    list_beach = beach.main(random_X, random_B, 10000)
    z=0
    enimg = np.zeros(shape=[height, width], dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            enimg[i, j] = bloco[i, j]^list_beach[z % len(list_beach)]
            z+=1

    enimg = cubo_rubik.imagem_permutada(enimg, k5, k6)
    return enimg


def  decript(imagem, random_X, random_B, linhas_permutadas_inversas, colunas_permutadas_inversas):
    imagem = cubo_rubik.decript(imagem, linhas_permutadas_inversas, colunas_permutadas_inversas)
    height = imagem.shape[0]
    width = imagem.shape[1]
    list_beach = beach.main(random_X, random_B, 10000)

    z=0
    decimg = np.zeros(shape=[height, width], dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            decimg[i, j] = imagem[i, j]^list_beach[z % len(list_beach)]
            z+=1
    return decimg

if __name__ == "__main__":
    imagem = cv2.imread('lena.png')
    enigma, x, y = main(imagem, 0.003, 0.983)
    plt.imshow(enigma)
    plt.show()
    imagem_ = decript(enigma, 0.003, 0.983, x, y)
    plt.imshow(imagem_)
    plt.show()




