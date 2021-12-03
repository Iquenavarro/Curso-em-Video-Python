#escreva um programa para ler dois numeros inteiros e dizer qual é maior ou se são iguais

num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero: '))

maior = num1

if  num1 > num2:
    print('O numero {} é maior que o numero {}.'.format(num1,num2))
elif num1 == num2:
    print('Os números são iguais.')
else:
    print('O numero {} é maior.'.format(num2))
