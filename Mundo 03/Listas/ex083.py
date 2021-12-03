''' Crie um programa onde o usuario digite um expressao qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada
está com os parênteses abertos e fechados na ordem correta
'''

lista = []
frase = str(input('Digite uma expressão matemática: '))

#lista = str.split(' ')
#print(lista)

for simbolo in frase:
    if simbolo == '(':
        lista.append(simbolo)
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop(-1)
        else:
            lista.append(')')
            break
print(f'Lista: {lista}')

if len(lista) == 0:
    print('Válida')
else:
    print('Inválido')