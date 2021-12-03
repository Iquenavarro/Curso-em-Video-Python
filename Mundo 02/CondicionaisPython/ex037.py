#leia um numero qualquer e faca a base de conversao

num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao
1 - Converter para Binário
2 - Converter para Octal
3 - Converter para Hexadecimal
''')

opcao = int(input('Sua opcao: '))

if opcao == 1:
    print('{} convertido para binário é igual a {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Digite uma opção válida')
