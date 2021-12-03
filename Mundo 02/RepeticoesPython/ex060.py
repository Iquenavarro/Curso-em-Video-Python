# faca um programa que calcule o fatorial

num = int(input('Digite um numero para descobrir o fatorial: '))
counter = num
fat = 1

print('Calculando {}! = '.format(num), end='')
while counter > 0:
    print('{}'.format(counter))
    fat *= counter
    counter -= 1
    print(' x ' if counter >= 1 else ' = ', end="")
print('{}'.format(fat))