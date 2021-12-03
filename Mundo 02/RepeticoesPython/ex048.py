#numeros impares e multiplos de 3 entre 1 e 500
soma = 0
cont = 0
for num in range(1, 501):
    if  num % 2 == 1:
        if num % 3 == 0:
            soma = soma + num
            cont = cont + 1

print('A soma de {} solicidados é {}'.format(cont, soma))

