#sorteio dos nomes
from random import shuffle

aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')

nomes = [aluno1, aluno2, aluno3, aluno4]
shuffle(nomes)

print('A lista de apresentação é {}.'.format(nomes))

