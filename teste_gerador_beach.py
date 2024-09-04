import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy
import beach

# Supondo que beach.main() gere a lista de números caóticos
random_numbers=  beach.main(0.33431231, 0.74234233, 10000)
# random_numbers =  teste_prng.main(10000)
print(random_numbers)
# Histograma
plt.hist(random_numbers, bins=50, color='blue', alpha=0.7)
plt.title("Histograma dos Números Caóticos Gerados")
plt.show()

# Autocorrelação


# Entropia
histogram, bin_edges = np.histogram(random_numbers, bins=256, density=True)
ent = entropy(histogram)
print(f"Entropia: {ent}")
# print(random_numbers)
