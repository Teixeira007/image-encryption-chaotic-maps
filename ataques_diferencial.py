import cv2

def uaci(original, cifrada):
    # Assumimos que a imagem é RGB com três canais.
    height, width, channels = original.shape
    value = 0
    
    for c in range(channels):
        for y in range(height):
            for x in range(width):
                value += abs(int(original[y, x, c]) - int(cifrada[y, x, c]))
    
    # Calculamos o valor médio para todos os canais
    value = value * 100 / (width * height * 255 * channels)
    return value


def npcr(imagem_original, imagem_modificada):
    # Assumimos que a imagem é RGB com três canais.
    height, width, channels = imagem_original.shape
    total_pixels = height * width * channels
    pixels_alterados = 0
    
    for c in range(channels):
        pixels_alterados += cv2.countNonZero(cv2.absdiff(imagem_original[:, :, c], imagem_modificada[:, :, c]))
    
    npcr_value = pixels_alterados / total_pixels * 100
    return npcr_value


enc_original = cv2.imread('imagens/img_cifrada_r_3.99.bmp')
enc_cifrada = cv2.imread('imagem_modificada_lena.bmp')
resultado_uaci  = uaci(enc_original, enc_cifrada)
print('UACI: ', resultado_uaci)

resultado_nrpc = npcr(enc_original, enc_cifrada)
print("NRPC: {:.4f}%".format(resultado_nrpc))
