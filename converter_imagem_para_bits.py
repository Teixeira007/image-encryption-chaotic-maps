import cv2

def image_to_bits(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    bits = ''.join(format(byte, '08b') for byte in image.flatten())
    return bits

# Exemplo de uso
encrypted_image_path = 'lena_cifrado__.bmp'
bit_sequence = image_to_bits(encrypted_image_path)

# Salvar a sequência de bits em um arquivo
with open('bit_sequence3.txt', 'w') as f:
    f.write(bit_sequence)
