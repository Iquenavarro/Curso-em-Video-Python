# programa que leia 5 valores e mostre qual é o maior qual o menor e suas posicoes na lista

listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite o valor para o numero {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
for i, v in enumerate(listanum):
    if v == maior:
        print(f'O maior valor está na posição {i}...')
    if v == menor:
        print(f'O menor valor está na posição {i}')


print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')

