#Leia o nome e o peso das pessoas e coloque em uma lista.
# No final mostre quantas as pessoas foram cadastradas.
# Quais foram as pesadas e as mais leves

pessoa = list()
galera = list()
maior = menor = 0
while True:
    pessoa.append(str(input('Digite um nome: ')))
    pessoa.append(float(input('Digite seu peso: ')))
    if len(galera) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] < menor:
            menor = pessoa[1]
        if pessoa[1] > maior:
            maior = pessoa[1]
    galera.append(pessoa[:])
    pessoa.clear()
    continuacao = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuacao not in 'SsNn':
        continuacao = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuacao == 'N':
        break
print(f'A lista é {pessoa} e tem {len(pessoa)} pessoas.')
print(f'A galera é {galera} e tem {len(galera)} pessoas.')
print(f'O maior peso é {maior} e o menor peso é {menor}')





