#leia um numero e descubra se ele é primo ou nao

n = int(input('Digite um numero inteiro: '))

primo = True
c = (n // 2)


for i in range(c, 0, -1):
    if n % i == 0 and i != 1:
        primo = False

if primo:
    print('O numero é primo', format(n))
else:
    print('O numero não é primo'. format(n))
