

p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razao da PA: '))
dec = p + (10 - 1)*r
counter = p
termo = 0
user = -1
tam = 10

while True:
    while counter < tam:
        termo += r
        counter += 1
        print(termo)
    user = int(input('Mais termos: '))

    if user == 0:
        break
    user += counter
    tam = user

print('Fim')




