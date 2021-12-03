#leia dois valores e mostre um menu na tela

num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

menu = (''''
Digite uma opção:\n
1 - Somar dois números 
2 - Multiplicar dois numeros 
3 - Maior dos numeros
4 - Novos Numeros
5 - Sair do programa
''')

maior = 0
menor = 0

print(menu)
user = int(input('Sua escolha: '))
while user != 5:
    if user > 5:
        print('Escolha um numero de 1 a 5.')
        user = int(input('Sua escolha: '))
    elif user < 0:
        print('Escolha um numero positivo e de 1 a 5.')
        user = int(input('Sua escolha: '))
    else: #caminho normal
        if user == 1:
            print('Voce escolheu somar!')
            print('Resultado da soma entre {} e {} é {}.'.format(num1, num2,(num1 + num2)))
            print(menu)
            user = int(input('Sua escolha: '))
        elif user == 2:
            print('Voce escolheu multiplicar')
            print('O resultado da multiplicação entre {} e {} é {}.'.format(num1, num2, (num1 * num2)))
            print(menu)
            user = int(input('Sua escolha: '))
        elif user == 3:
            print('Voce escolheu descobrir qual é o maior dos numeros')
            if num1 > num2:
                maior = num1
                menor = num2
                print('O maior dos numeros é o numero {} e o menor é o número {}.'.format(num1, num2))
                print(menu)
                user = int(input('Sua escolha: '))
            elif num2 > num1:
                maior = num2
                menor = num1
                print('O maior dos numeros é o numero {} e o menor é o numero {}.'.format(num2, num1))
                print(menu)
                user = int(input('Sua escolha: '))

            else:
                print('Os dois números são identicos')
                print(menu)
                user = int(input('Sua escolha: '))
        elif user == 4:
            nnum1 = float(input('Novo numero 1: '))
            nnum2 = float(input('Novo numero 2: '))
            num1 = nnum1
            num2 = nnum2
            print(menu)
            user= int(input('Sua escolha: '))
print('Opcao 5: Programa encerrado')