#leia varios numeros e coloque em uma lista, quantos numeros foram digitados, a lista decrescente e se o valor 5 foi digitado ou nao

counter = 0
lista = []

while True:
    num = int(input('Digite um numero: '))
    if num not in lista:
        lista.append(num)
        counter += 1
    continuacao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if  continuacao not in "SsNn":
        continuacao = str(input('Valor Inválido, digite somente Sim ou Não. Deseja Continuar [S/N]? ')).strip().upper()[0]
    if continuacao == "N":
        break
lista.sort(reverse=True)
print(f'A lista contem {counter} numeros e é a seguinte: {lista}')

print(f'Voce digitou {len(lista)}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista')


