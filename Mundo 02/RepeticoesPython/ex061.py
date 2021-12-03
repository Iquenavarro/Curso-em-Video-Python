

p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razao da PA: '))
dec = p + (10 - 1)*r
counter = p
while counter <= dec:
    print('{}'.format(counter))
    counter += r
print('FIM')




