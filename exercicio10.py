
import random

# Sortear 6 números entre 1 e 60
numeros = random.sample(range(1, 61), 6)

# Organizar os números em ordem crescente
numeros.sort()

# Exibir o resultado
print("Números sorteados da Mega-Sena:")
print(numeros)

