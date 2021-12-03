#escreva um nome e retorne o primeiro nome e o ultimo

nome = str (input('Digite um nome: '))

nomestring = nome.split()

print('Primeiro nome é {} e o ultimo nome é {}.'.format(nomestring[0], nomestring[-1]))