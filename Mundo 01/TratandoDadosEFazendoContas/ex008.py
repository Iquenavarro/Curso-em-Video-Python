#leia um valor de distância em metros e exiba em cm e mm

num1 = float(input('Digite um número: '))

cmnum = num1*100

mmnum = num1*1000

print('O numero é equivalente a {} cm e a {} milimetros.'.format(cmnum, mmnum))
