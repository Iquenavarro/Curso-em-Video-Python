# sortear um aluno
import random

aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')

nomes = [aluno1, aluno2, aluno3, aluno4]

sorteado = random.choice(nomes)
print('O aluno escolhido é {}.'.format(sorteado))



