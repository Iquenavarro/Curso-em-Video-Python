#leia varios numeros pelo teclado e mostre a media entre os valores, o maior o menor numero

flag = False
counter = somador = media = maior = menor = 0

while flag == False:
    num = int(input('Digite um numero inteiro: '))

    #media
    somador += num
    counter += 1
    media = (somador / counter)

    #Maior/Menor
    if num > maior:
        maior = num
    if menor == 0:
        menor = num
    if num < menor:
        menor = num

    #continuacao
    cont = str(input('Quer Continuar? [SIM / NÃO] ')).strip().upper()
    if cont == "NÃO":
        flag = True

print('Media: {:.1f}'.format(media))
print('Maior: {} | Menor: {}'.format(maior, menor))