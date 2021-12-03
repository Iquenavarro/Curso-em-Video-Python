'''
Aprimore o 086 mostrando no final A soma de todos os valores pares digitados.
A soma dos valores da terceira coluna.
O maior valor da segunda linha
'''

lista = list()
listab = list()

for i in range (0, 3):
    for j in range (0, 3):
        listab.append(int(input(f'Digite um valor para [{i}, {j}]: ')))

    lista.append(listab[:])
    listab.clear()

for l in lista:
    print(l)

#soma de todos os valores pares digitados
somapar = 0

for i in range(3):
    for j in range(3):
        if lista[i][j] % 2 == 0:
            somapar += lista[i][j]
print(f'Soma dos valores pares é: {somapar}')

#soma dos valores da terceira coluna
somacoluna = 0
for i in range(3):
    for j in range(3):
        if j == 2:
            somacoluna += lista[i][j]
print(f'Soma da terceira coluna é: {somacoluna}')

#O maior valor da segunda linha

maior = 0

for i in range(3):
    for j in range(3):
        if i == 1:
            if lista[i][j] > maior:
                maior = lista[i][j]
print(f'Maior valor da segunda linha: {maior}')