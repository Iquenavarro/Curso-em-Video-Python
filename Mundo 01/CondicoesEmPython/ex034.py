# pergunte o salario e atribua o aumento

salario = float(input('Qual é o seu salário? '))

if salario > 1250:
    fator = 0.1
else:
    fator = 0.15

aumento = salario*(1 + fator)

print('O seu salario novo é: R$ {:.2f}.'.format(aumento))

