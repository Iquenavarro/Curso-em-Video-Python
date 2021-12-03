# melhore o desafio 28

import random
num1 = random.randint(0, 5)

num = int(input('Adivinhe um numero de 0 a 5: '))
counter = 0

while num != num1:
    if num < 0 or num > 5:
        if num < 0:
            print('O numero não pode ser negativo')
        elif num > 5:
            print('Tente um número menor do que 6!')
            num = int(input('Digite: '))
    else:
        if num != num1:
            if num1 > num:
                print('Você errou! \nDica: digite um número maior.')
                print('Numero digitado: {}.'.format(num))
                num = int(input('Tente novamente: \n'))
            elif num1 < num:
                print('Você errou! \nDica: digite um número menor.')
                print('Numero digitado: {}.'.format(num))
                num = int(input('Tente novamente: \n'))
    counter += 1

print('Numero digitado: {}.'.format(num))
print('Numero do sorteador: {}'.format(num1))
print('Parabens, você venceu ')
print('Numero de tentativas: {}'.format(counter))






