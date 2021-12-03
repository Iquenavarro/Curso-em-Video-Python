# programa pro usuario adivinhar um numero que o computador adivinhou
import random
num1 = random.randint(0, 5)

num = int(input('Adivinhe um numero de 0 a 5: '))

if num == num1:
    print('Parabens você acertou')
else:
    print('Tente novamente')
