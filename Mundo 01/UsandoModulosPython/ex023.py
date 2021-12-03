#Estudar como faz com string

#num = int(input('Informe um numero: '))
#n = str(num)

#print('Analisando o numero {}'. format(num))
#print('Unidade {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))

nums = int(input("Digite um número a ser fatiado: \n"))

us = nums // 1 % 10
ds = nums // 10 % 10
cs = nums // 100 % 10
ms = nums // 1000 % 10

print('Unidade: {}.'.format(us))
print('Dezena: {}.'.format(ds))
print('Centena: {}.'.format(cs))
print('Milhar: {}.'.format(ms))