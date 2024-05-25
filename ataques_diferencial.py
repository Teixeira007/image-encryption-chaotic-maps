import cv2
def uaci(original, cifrada):
    height, width = original.shape
    value=0
    for y in range(height):
        for x in range(width):
            value +=(abs(int(original[x,y])-int(cifrada[x,y])))
    value = value*100/(width*height*255)
    return value

enc_original = cv2.imread('imagens/sensibilidade_a_chave/img_cifrada_chave_0.001985_0.153972.bmp', cv2.IMREAD_GRAYSCALE)
enc_cifrada = cv2.imread('imagens/sensibilidade_a_chave/img_cifrada_chave_totalmente_diferente.bmp', cv2.IMREAD_GRAYSCALE)
print('UACI: ', uaci(enc_original, enc_cifrada))
# imagem = cv2.imread("lena.png")

# # Coordenadas do pixel a ser modificado (x, y)
# x = 100
# y = 200

# # Novo valor do pixel (BGR format)
# novo_valor_pixel = (0, 0, 0)  # Exemplo: vermelho (BGR)

# # Modificar o pixel
# imagem[y, x] = novo_valor_pixel

# # Salvar a imagem modificada
# cv2.imwrite("imagem_modificada.bmp", imagem)
def nrpc(imagem_original, imagem_modificada):
    total_pixels = imagem_original.shape[0] * imagem_original.shape[1]
    pixels_alterados = cv2.countNonZero(cv2.absdiff(imagem_original, imagem_modificada))
    nrpc_value = pixels_alterados / total_pixels * 100
    return nrpc_value



resultado_nrpc = nrpc(enc_original, enc_cifrada)
print("NRPC: {:.2f}%".format(resultado_nrpc))