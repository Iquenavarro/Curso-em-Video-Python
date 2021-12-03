# leia 3 retas e determine se elas podem ser um triangulo

a = float(input('Digite um lado do triangulo: '))
b = float(input('Digite outro lado do triangulo: '))
c = float(input('Digite o terceiro lado do triangulo: '))

if a + b > c and a + c > b and b + c > a:
    print('O triangulo existe')
else:
    print('O triangulo não existe')
