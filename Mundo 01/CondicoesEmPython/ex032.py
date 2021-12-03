# faca um programa que leia se o ano é bissexto

ano = int(input('Digite um ano: '))

u = ano // 1% 10
d = ano // 10 % 10

dez = u + d*10

if dez % 4 == 0:
    print('O ano é bissexto')

else:
   print('O ano não é bissexto')

