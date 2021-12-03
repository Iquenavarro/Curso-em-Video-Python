#faca um programa que auxilie um jogador a criar palpites para a mega sena
from random import randint
from time import sleep
palpites = int(input('Digite quantos palpites você quer: '))
lista = list()
jogos = list()
counter = 0
total = 1


while total <= palpites:
    counter = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            counter += 1
        if counter >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
    
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(.5)