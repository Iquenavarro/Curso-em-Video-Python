#elabore um programa que de desconto a partir da forma de pagamento

valor = float(input('Digite o valor: R$ '))
print('''
Digite 1 = Pagamento Dinheiro
Digite 2 = Pagamento Cheque 
Digite 3 = Á Vista Cartão 
Digite 4 = Cartão Crédito 1x 
Digite 5 = Cartão Crédito 2x
Digite 6 = Cartão Crédito 3x ou mais
''')
fpagamento = int(input('Digite uma forma de pagamento: '))

if fpagamento == 1 or fpagamento == 2:
    desconto = - 0.1
elif fpagamento == 3:
    desconto = -0.05
elif fpagamento == 4 or fpagamento == 5:
    desconto = 0.0
else:
    desconto = 0.2

apagar = valor * (1 + desconto)

print('O valor a pagar é R$ {:.2f}.'.format(apagar))

