#Mostre a tabuada de varios numeros quando inserido um numero negativo o programa para
c = 0
while True:
    n = int(input('Digite um numero para ver a tabuada [Digite um número negativo para parar]: '))
    if n < 0:
        break
    for i in range(1, 11):
        print('{} x {} = {}'.format(n, i , n*i))

    c += 1
print(f'Você calculou {c} tabuadas')

print('Programa Encerrado')

