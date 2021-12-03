#escreva um programa que vai aprovar um emprestimo bancario
#pergunte salario, valor da casa e quantos anos vai pagar, sabendo que a parcela nao pode exceder 30% do salario

salario = float(input('Qual é o seu salário? R$ '))
casa = float(input('Qual é o valor da casa? R$ '))
anos = int(input('Quantos anos vai pagar? '))

parcela = casa / (12*anos)
parcelamax = salario*0.3

if  parcela > parcelamax:
    print('O emprestimo foi recusado, amplie o seu periodo de pagamento, o valor da parcela seria de {} e o seu limite é {}.'.format(parcela, parcelamax))
      

else:
    print('O emprestimo foi aprovado, valor da parcela {}.'.format(parcela))