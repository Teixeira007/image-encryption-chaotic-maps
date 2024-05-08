import numpy as np
import math
import struct
def logistic_map(B0):
    return np.minimum(4 * B0 * (1 - B0), 10000)


def map_C(B, x):
    while x <0 or x > 1:
        x = np.random.rand()
    while B == 1 or B<0:
        B = np.random.rand()

    result = (B - x * B**x - (1 - x) * B**(1 - x) * B) / (B - np.sqrt(B))
    return result


def generate_sequence(X0, B0, num):
    n = 0
    
    while n < num:
        B_next = logistic_map(B0)
        
        if B_next < 1e-4:
            B_next = map_C(1 / B_next, X0)
            if B_next < 1e-4:
                B_next = 1e-4
            X_next = map_C(1 / B_next, X0)
        else:
            X_next = map_C(1 / B_next, X0)

        X_next = abs(X_next)  # Garante que X_next seja positivo
        X_next -= int(X_next)  # Garante que X_next esteja no intervalo [0, 1)
        
        n = n + 1  
        if n == num:
            z = X_next
        
        B0 = B_next
        X0 = X_next
    return z

    
# MAIN
list = []    
for i in range(100):
    
    num = 100
    X0 = np.random.rand()
    B0 = np.random.rand()
    while B0 == 0 or B0 == 0.75 or B0 == 1:
            B0 = np.random.rand()
        
    num_random = generate_sequence(X0, B0, num)
    list.append(num_random)

print(list)

with open('numeros_binarios_v0.txt', 'w') as f:
    # Para cada número decimal, convertemos para o formato binário e escrevemos no arquivo de texto
    for numero in list:
        # Usando o método pack da biblioteca struct para converter o número em binário
        numero_binario = struct.pack('f', numero)
        numero_binario_str = ''.join(format(byte, '08b') for byte in numero_binario)
        f.write(numero_binario_str + '\n')

