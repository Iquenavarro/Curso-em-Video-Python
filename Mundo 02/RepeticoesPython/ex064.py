#leia varios numeros inteiros pelo teclado

num = print('Digite um numero: ')

alerta = False
somador = 0
counter = 0

while alerta == False:
    num = int(input('Digite um numero [999 para parar]: '))
    if num == 999:
        alerta = True
    else:
        somador += num
        counter += 1
print('Soma: {}'. format(somador))
print('Numeros digitados: {}'.format(counter))

