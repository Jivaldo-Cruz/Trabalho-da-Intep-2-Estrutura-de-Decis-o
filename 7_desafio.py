__autor__ = "Jivaldo Da Cruz"

import math

lista = []

print("Digite 3 números para saber qual é o maior")
for x in range(3):
    lista.append(float(input(f"Informe {x + 1}º número: ")))

#Usei função max() e min() -> para saber qual é o maior e o menor número da lista
print(f"O maior número é {max(lista)}")
print(f"O menor número é {min(lista)}")
