import cv2

def image_to_bits(image_path):
    image = cv2.imread(image_path)
    bits = ''.join(format(byte, '08b') for byte in image.flatten())
    return bits

# Exemplo de uso
encrypted_image_path = 'img_cifrada_chave_0.1987_0.73974_76453454.0_534675657.0.bmp'
bit_sequence = image_to_bits(encrypted_image_path)

# Salvar a sequência de bits em um arquivo
with open('bit_sequence.txt', 'w') as f:
    f.write(bit_sequence)
