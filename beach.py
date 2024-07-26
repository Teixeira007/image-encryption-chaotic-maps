import numpy as np

def logistic_map(B0):
    return  4 * B0 * (1 - B0)


def map_b_exponencial(B, x):
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
            B_next = map_b_exponencial(1 / B_next, X0)
            if B_next < 1e-4:
                B_next = 1e-4
            X_next = map_b_exponencial(1 / B_next, X0)
        else:
            X_next = map_b_exponencial(1 / B_next, X0)

        X_next = abs(X_next)  # Garante que X_next seja positivo
        X_next %= 1  # Garante que X_next esteja no intervalo [0, 1)
        
        n = n + 1  
        if n == num:
            z = X_next
        
        B0 = B_next
        X0 = X_next
    return z, B0

    
# MAIN
def main(X0, B0, size):
    list = []    
    for i in range(size):
        
        num = 50
        X0, B0 = generate_sequence(X0, B0, num)
        list.append(int(X0 * pow(2,56)) % 255)

    return list


def keygen(x, size):
    key = []
    for i in range(size):
        x = 4 * x * (1-x)
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
        x = 4 * x * (1 - x)
        seq.append(x)
    return np.array(seq)

def chaotic_permutation(dimensao, key):
    seq  = logistica_map_permutation(key, dimensao)
    return np.argsort(seq)

if __name__ == "__main__":
    # list = main(0.5, 0.653, 100)
    keygen_int(0.001, 3.915, 2)
