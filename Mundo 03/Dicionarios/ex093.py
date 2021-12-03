'''
Programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai lert o nome do jogador e quantas partidas ele jogou.
Quantos gols ele fez em cada partida. Mostre no final o total de gols que ele fez.
'''

aproveitamento = dict()
partidas = list()

gols = 0

#insere um nome no dicionario

aproveitamento['nome'] = str(input('Qual o nome do jogador: '))

#partidas23

aproveitamento['partidas'] = int(input('Quantas partidas foram disputadas? '))

#gols em partidas

for partida in range(aproveitamento['partidas']):
    partidas.append(int(input(f'Quantos gols foram marcados pelo {aproveitamento["nome"]} fez na {partida + 1} ? ')))

aproveitamento['gols'] = partidas[:]
aproveitamento['total'] = sum(partidas)

for k, v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}')
print('-='* 30)
print(f'o jogador {aproveitamento["nome"]} jogou {len(aproveitamento["gols"])} partidas.')

for i, v in enumerate(aproveitamento["gols"]):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {aproveitamento["total"]} gols.')


