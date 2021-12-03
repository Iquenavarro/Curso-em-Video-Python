# Crie um programa que leia o nome completo da pessoa e mostre com todas as letras maiusculas, minusculas  quantas letras ao todo

nome = str(input('Digite seu nome: ')).strip()

nmai = nome.upper()

nmin = nome.lower()

comp = len(nome)-nome.count(" ") #verificar

firstname = nome.split()

print('O nome em maiusculo {}.'.format(nmai))
print('O nome em minusculo é {}.'.format(nmin))
print('O nome tem {} caracteres.'.format(comp))
print('O primeiro nome é {} e ele tem {} letras.'.format(firstname[0], len(firstname[0])))
