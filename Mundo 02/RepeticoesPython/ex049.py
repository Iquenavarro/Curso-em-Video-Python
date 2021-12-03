#refaca o desafio 9 com o laço for

num = int(input('Digite um numero: '))


for i in range (1, 11):
    print('{} x {:2} = {}'.format(num, i, i*num))

