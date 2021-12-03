lista = []

while True:
    num = int(input('Digite um numero: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, tente novamente!')
    continuacao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while continuacao not in "SsNn":
        continuacao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuacao == "N":
        break
lista.sort()
print(f'Você digitou os valores {lista} ')
