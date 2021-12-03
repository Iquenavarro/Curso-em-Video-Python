#leia 6 numeros inteiros e faca a soma dos que sao inteiros

s = 0
cont = 0
for i in range (0, 6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        s +=num
        cont = cont + 1
print('Você informou {} numeros pares e a soma foi {}.'.format(cont, s))

