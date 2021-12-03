#programa para jogar jokenpo

import random

print('''
Digite 1 = Pedra
Digite 2 = Papel 
Digite 3 = Tesoura 

''')
jokenpo = int(input('Digite um numero para Escolher: '))

escolhas = ["Pedra", "Papel", "Tesoura"]
esc1 = random.choice(escolhas)

if jokenpo == 1:
    if esc1 == "Pedra":
        print('Empate, o computador escolheu {}.'.format(esc1))
    elif esc1 == "Papel":
        print('Você perdeu, o computador escolheu {}, tente novamente'.format(esc1))
    elif esc1 == "Tesoura":
        print('Você ganhou, o computador escolheu {}, parabéns'.format(esc1))
elif jokenpo == 2:
    if esc1 == "Papel":
        print('Empate, o computador escolheu {}'.format(esc1))
    elif esc1 == "Tesoura":
        print('Você perdeu, o computador escolheu {}, tente novamente'.format(esc1))
    elif esc1 == "Pedra" :
        print('Você ganhou, o computador escolheu {}, parabéns!'.format(esc1))

elif jokenpo == 3:
    if esc1 == "Tesoura":
        print('Empate, o computador escolheu {}'.format(esc1))
    elif esc1 == "Pedra":
        print('Você perdeu, o computador escolheu {}, tente novamente'.format(esc1))
    elif esc1 == "Papel":
        print('Você ganhou, o computador escolheu {}, parabens'.format(esc1))

