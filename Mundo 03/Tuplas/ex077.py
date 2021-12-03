#tupla com varias palavras e mostre quais sao as vogais

lista = ('Batata', 'Cebola', 'Alface', 'Joaquim', 'Cristiano', 'Tablet', 'Celular', 'Hamburguer')


for p in lista:
    print(f'\nNa Palavra {p.upper()} temos ', end='')
    for lista in p:
        if lista.lower() in 'aeiou':
            print(lista, end='')

