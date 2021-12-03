'''Varios numeros e colocar em uma lista,
crie duas listas extras que vao conter apenas os valores pares
e os valores impares digitados respectivamente.
Ao final mostre o conteudo das tres listas geradas.'''

lista = []
par = []
impar = []

while True:
    num = int(input('Digite um numero: '))
    if num not in lista:
        lista.append(num)
    if num % 2 == 0:
        if num not in par:
            par.append(num)
    elif num % 2 == 1:
        if num not in impar:
            impar.append(num)
    continuacao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuacao not in 'SsNn':
        continuacao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuacao == 'N':
        break

print(f'A lista contem {lista} os números pares dela são {par} e os números ímpares são {impar}')

