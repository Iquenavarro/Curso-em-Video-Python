#programa para escrever os numeros pares de 2 a 50

for num in range (1, 51):
    if  num % 2 == 0:
        print(num)

#versao alternativa
print('Versao alternativa')
for num in range(2, 51, 2):
    print(num)

