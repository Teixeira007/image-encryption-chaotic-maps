import cv2
import numpy as np

def uaci(original, cifrada):
    diff = np.abs(original.astype(np.int16) - cifrada.astype(np.int16))
    uaci = np.mean(diff) / 255 * 100
    return uaci


def npcr(imagem_original, imagem_modificada):
    diff = imagem_original != imagem_modificada
    npcr = np.sum(diff) / diff.size * 100
    return npcr


enc_original = cv2.imread('lena_cifrado__.bmp', cv2.IMREAD_GRAYSCALE)
enc_cifrada = cv2.imread('lena_cifrado_1pixel.bmp', cv2.IMREAD_GRAYSCALE)

resultado_uaci  = uaci(enc_original, enc_cifrada)
print('UACI: ', resultado_uaci)

resultado_nrpc = npcr(enc_original, enc_cifrada)
print("NRPC: {:.4f}%".format(resultado_nrpc))
