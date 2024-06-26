import numpy as np
import matplotlib.pyplot as plt
import beach



def plot_logistic_map(r, x0, num_iterations):
    x = np.zeros(num_iterations)
    x[0] = x0
    
    for i in range(1, num_iterations):
        x[i] = beach.logistic_map(r, x[i-1])
    
    plt.figure(figsize=(6, 4))
    plt.plot(range(num_iterations), x, marker='o', linestyle='-', color='b')
    plt.title(f'r = {r}')
    plt.xlabel('Iterações')
    plt.ylabel('x')
    plt.grid(True)
    plt.show()



def plot_beach(list):
    plt.figure(figsize=(12, 6))
    plt.plot(list, marker='o', linestyle='-', color='b')
    plt.title('Comportamento Iterativo do Algoritmo')
    plt.xlabel('Iterações')
    plt.ylabel('X')
    plt.grid(True)
    plt.show()

list = beach.main(0.0876, 0.353, 100)
plot_beach(list)
# plot_logistic_map(3.9, 0.08, 100)
