import numpy as np
import math
import struct
def logistic_map(B0):
    return np.minimum(3.195 * B0 * (1 - B0), 10000)


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
    return z, B0

    
# MAIN
def main(X0, B0, size):
    list = []    
    for i in range(size):
        
        num = 50
        # X0 = np.random.rand()
        # B0 = np.random.rand()
        # while B0 == 0 or B0 == 0.75 or B0 == 1:
        #         B0 = np.random.rand()
            
        X0, B0 = generate_sequence(X0, B0, num)
        list.append(int(X0 * pow(2,56)) % 256)

    binary_list  = decimal_to_binary_list(list)
    write_binary_list_to_file(binary_list, 'numeros_binarios.txt')
    return list

def decimal_to_binary_list(decimal_numbers):
    # Convert each decimal number to binary using bin() function
    binary_list = [bin(num)[2:] for num in decimal_numbers]
    return binary_list

def write_binary_list_to_file(binary_list, filename):
    with open(filename, "w") as file:
        for binary_str in binary_list:
            file.write(binary_str + "\n")

def keygen(x, r, size):
    key = []
    for i in range(size):
        x = r * x * (1-x)
        key.append(x)
    return key

def keygen_int(x, r, size):
    key = []
    for i in range(size):
        x = r * x * (1-x)
        key.append(int(x * pow(10,16)) % 6)
    print(key)
    return key

if __name__ == "__main__":
    # main(0.001, 0.653, 100)
    keygen_int(0.001, 3.915, 70)
