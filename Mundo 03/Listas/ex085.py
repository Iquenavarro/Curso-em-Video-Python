'''
Usuario digita 7 valores
e os cadastre em uma lista única que mantenha os valores pares
e impares separados em ordem crescente.

'''
lista = [[], []]

for p in range (0, 7):
    numero = int(input('Digite um numero inteiro: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    elif numero % 2 == 1:
        lista[1].append(numero)
print(f'Numero pares em orodem crescente: {sorted(lista[0])}')
print(f'Numero impares em ordem crescente: {sorted(lista[1])}')

