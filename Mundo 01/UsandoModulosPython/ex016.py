#programa que leia um numero real qualuqer e mostre a porção inteira
import math
num = float(input('Digite um número qualquer: '))

numint = math.trunc(num)

print('A porção inteira do número é {}'.format(numint))


