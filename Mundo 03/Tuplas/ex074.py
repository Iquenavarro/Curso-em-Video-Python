#tupla de numeros aleatorios

import random

aleatorios = []
counter = 0

while counter < 5:
    aleatorios.append(random.randint(0, 100))
    counter += 1

aleatorios = tuple(aleatorios)


#maior e menor

maior = aleatorios[0]
menor = aleatorios[0]

for num in aleatorios:
    if num < menor:
        menor = num
    if num > maior:
        maior = num

print(f'Maior é {maior} e o menor é {menor}')
print(f'A tupla é {aleatorios}')