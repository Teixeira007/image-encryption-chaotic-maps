import numpy as np
from collections import Counter

def logistic_map(B0):
    return  3.99 * B0 * (1 - B0)

def map_b_exponencial(B, x):
    if x <0 or x > 1:
        x = normalize_to_unit_interval(x)
    if B >= 1 or B<0:
        B = normalize_to_unit_interval(B)

    result = (B - x * B**x - (1 - x) * B**(1 - x) * B) / (B - np.sqrt(B))
    return result

def henon_map(x, y, a=1.4, b=0.3):
    return 1 - a * x**2 + y, b * x


def generate_sequence(X0, B0, num):
    n = 0
    
    while n < num:
        # Várias iterações de mapas caóticos
        
        B_next = logistic_map(B0)
        x_next, y_next = henon_map(X0, B_next)
        X0, B0 = x_next, y_next

        
        if B_next < 1e-4:
            B_next = map_b_exponencial(1 / B_next, X0)
            if B_next < 1e-4:
                B_next = 1e-4
            X_next = map_b_exponencial(1 / B_next, X0)
        else:
            X_next = map_b_exponencial(1 / B_next, X0)

        X_next = (X_next + y_next + B_next) / 3
        X_next = abs(X_next)
        X_next %= 1
        
        n += 1  
        if n == num:
            z = X_next
        
        B0 = B_next
        X0 = X_next

    return z, B0

# MAIN
def main(X0, B0, size):
    list = []    
    for i in range(size):
        
        num = 10
        X0, B0 = generate_sequence(X0, B0, num)
        # valor = int(X0 * 1000) % 255

        valor = int((X0 * 1e6 + B0 * 1e6) % 256)
        
        list.append(valor)
    limite_pico = 30
    contagem = Counter(list)

    valores_ajustados = []
    
    # Adicionar valores à lista ajustada, respeitando o limite
    for valor in list:
        if contagem[valor] > limite_pico:
            if valores_ajustados.count(valor) < limite_pico:
                valores_ajustados.append(valor)
        else:
            valores_ajustados.append(valor)

    return valores_ajustados

def keygen(x, size):
    key = []
    for i in range(size):
        x = 3.99 * x * (1 - x) 
        key.append(x) 
    return key

def keygen_int(x, r, size):
    key = []
    for i in range(size):
        x = r * x * (1-x)
        key.append(int(x * pow(10,16)) % 6)
    print(key)
    return key


def logistica_map_permutation(x, dimensao):
    seq = []
    for _ in range(dimensao):
        x = 3.99 * x * (1 - x)
        seq.append(x)
    return np.array(seq)

def chaotic_permutation(dimensao, key):
    seq  = logistica_map_permutation(key, dimensao)
    return np.argsort(seq)

def normalize_to_unit_interval(value):
    value = abs(value)  # Torna o valor positivo
    value %= 1  # Aplica o módulo para garantir que o valor esteja no intervalo [0, 1)
    if value == 0:
        value = 1e-10  # Evita valores exatamente 0
    return value

if __name__ == "__main__":
    list = main(0.1231231, 0.94234233, 1000)
    # keygen_int(0.001, 3.915, 2)
    # teste()
    
