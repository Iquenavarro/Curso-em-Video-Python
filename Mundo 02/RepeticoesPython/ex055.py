#  Faca o programa que leia o peso de 5 pessoas e qual foi o menor e qual foi o maior

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input('Digite um peso da {} pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso


print('O maior peso é {} kg.'.format(maior))
print('O menor peso é {} kg'.format(menor))
