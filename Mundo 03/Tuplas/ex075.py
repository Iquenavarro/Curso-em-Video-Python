#guardar 04 valores em uma tupla, valores que serão informados pelo usuário

counter = 0
tupla = []
while counter < 5:
    num = int(input('Digite um numero: '))

    counter += 1

    tupla.append(num)

tupla = tuple(tupla)


print(f'A sua lista é {tupla}')
print(f'O numero nove aparece {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O numero três aparece na {tupla.index(3)+1} posição')
else:
    print(f'O valor três não foi digitado em nenhuma posicao!')
pares = []

for num in tupla:
    if num % 2 == 0:
        pares.append(num)
print(f'Numeros pares são {pares}')
