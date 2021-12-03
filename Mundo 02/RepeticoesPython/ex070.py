#leia o nome e o preço de varios produtos

s = m1000 = 0
maior = 0
menor = 0
nome_menor = ''
while True:
    nome = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o preço do produto? '))
    s += preco

    if preco > 1000:
        m1000 += 1
    if menor == 0:
        menor = preco
        nome_menor = nome

    continuacao = str(input('Deseja continuar [S/N] ? ')).strip().upper()[0]

    if continuacao == 'N':
        print(f'O produto mais barato é {nome_menor} e custa {menor}')
        print(f'O total gasto foi: R$ {s:.2f}')
        print(f'{m1000} produtos custam mais de R$ 1000,00')
        break


