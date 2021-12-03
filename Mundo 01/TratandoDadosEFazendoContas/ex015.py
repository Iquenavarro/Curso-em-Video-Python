#carro alugado custa 60 por dia e 0,15 por km rodado
dias = int(input('Quantos dias utilizou o carro? '))
km = float(input('Quantos km foram rodados? '))

custo = dias*60 + km*0.15

print('O valor total a pagar é R$ {:.2f}.'.format(custo))