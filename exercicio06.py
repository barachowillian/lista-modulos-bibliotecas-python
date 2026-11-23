
import random

numero = random.randint(1, 100)

filmes = [
    "Titanic",
    "Avatar",
    "Barbie",
    "Interestelar",
    "Shrek"
]

print("Número sorteado:", numero)

filme = random.choice(filmes)
print("Filme escolhido:", filme)

random.shuffle(filmes)
print("Lista de filmes embaralhada:", filmes)

