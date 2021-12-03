#calcule o preco da passagem

num = int(input('Qual é a distância que deseja percorrer: '))

if  num <= 200:
    preco = num*0.5
    print('O custo da viagem será de: R$ {}.'.format(preco))
else:
    preco2 = num*0.45
    print('O custo da viagem será de: R$ {}.'.format(preco2))

