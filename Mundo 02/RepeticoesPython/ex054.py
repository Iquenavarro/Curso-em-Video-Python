#leia 7 idades e mostre quantos nao tem maioridade
from datetime import date

atual = date.today().year
counter_young = 0
counter_adult = 0


for i in range(1, 8):
    idade = int(input('Em que ano a {} pessoa nasceu? '.format(i)))
    if atual - idade >= 21:
        counter_adult += 1
    elif atual - idade < 21:
        counter_young += 1
print('Ao todo tivemos {} maiores e {} menores'.format(counter_adult, counter_young))

