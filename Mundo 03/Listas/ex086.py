'''
Crie uma matriz de 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela com a formatação correta
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
