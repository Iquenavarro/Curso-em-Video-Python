#leia um numero inteiro e mostre sua tabuada

num = int(input('Digite um numero: '))


for i in range (num, num*11, num):
    print('{} x {:.0f} = {}'.format(num,(i/num),i))


