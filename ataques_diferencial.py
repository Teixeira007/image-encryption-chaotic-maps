import cv2

def uaci(original, cifrada):
    # Assumimos que a imagem é em tons de cinza com apenas um canal.
    height, width = original.shape
    value = 0


    for y in range(height):
          for x in range(width):
            value += abs(int(original[y, x]) - int(cifrada[y, x]))
    
    # Calculamos o valor médio para a imagem em tons de cinza
    value = value * 100 / (width * height * 255)
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


enc_original = cv2.imread('imagens/lena_cifrado.bmp')
enc_cifrada = cv2.imread('modificada.bmp')
imagem_cinza_original = cv2.cvtColor(enc_original, cv2.COLOR_BGR2GRAY)
imagem_cinza_cifrada = cv2.cvtColor(enc_cifrada, cv2.COLOR_BGR2GRAY)
resultado_uaci  = uaci(imagem_cinza_original, imagem_cinza_cifrada)
print('UACI: ', resultado_uaci)

resultado_nrpc = npcr(enc_original, enc_cifrada)
print("NRPC: {:.4f}%".format(resultado_nrpc))
