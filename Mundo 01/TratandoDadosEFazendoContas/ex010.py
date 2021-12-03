#programa para ler quanto dinheiro a pessoa tem e quantos dolares ela pode sacar

num1 = float(input('Qual o valor que tem disponível? R$ '))

divisor = num1 / (3.27)

print('O valor disponível para saque é $ {:.2f}.'.format(divisor))
