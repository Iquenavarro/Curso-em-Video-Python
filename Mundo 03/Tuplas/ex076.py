#crie uma tupla com nome e lista de preços

nomes = ('Batata', 2,
         'Cebola', 1,
         'Celular', 2000,
         'Televisão', 4000,
         'Mochila', 700,
         'Tablet', 1500)
print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 30)
for pos in range (0, len(nomes)):
    if pos % 2 == 0:
        print(f'{nomes[pos]:.<30}', end = '')
    else:
        print(f'R${nomes[pos]:>9.2f}')



