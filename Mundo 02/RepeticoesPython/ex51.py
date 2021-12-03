#leia o primeiro termo e a razao da PA mostre os primeiros 10 numeros

p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razao da PA: '))
dec = p + (10 - 1)*r
for i in range (p, dec, r):
   print('{}'. format(i))



