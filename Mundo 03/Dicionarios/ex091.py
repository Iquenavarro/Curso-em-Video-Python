'''
Crie um programa onde 04 jogadores joguem um dado e tenham resultados aleatorios(Com pausas), ordene e mostre quem foi o maior valor

'''

from time import sleep
from random import randint
from operator import itemgetter

resultados = list()

jogo = {'jogador 1': randint(1,6),
        'jogador 2': randint(1,6),
        'jogador 3': randint(1,6),
        'jogador 4': randint(1,6)

        }

print('Valores sorteados: ')

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

resultados = sorted(jogo.items(), key= itemgetter(1), reverse=True)
print('== RANKING DOS JOGADORES ==')

for i, v in enumerate(resultados):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')



