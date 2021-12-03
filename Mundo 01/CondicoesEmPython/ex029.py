#leia a velocidade de um carro e informe se a multa

vel = int(input('Qual a velocidade (km/h): '))

if  vel > 80:
    multa = (vel - 80)*7
    print('O valor da multa é R$ {}.'.format(multa))
else:
    print('Velocidade dentro do permitido')



