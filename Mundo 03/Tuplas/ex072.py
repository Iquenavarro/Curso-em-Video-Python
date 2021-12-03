# Tupla preenchida com uma contagem por extenso, usuario digita entre 0 e 20 e preenche a tupla

extenso = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
           'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um numero de 1 a 20: '))
while num > 20 or num < 0:
    num = int(input('Tente novamente! Digite somente numeros entre 0 e 20: '))

print(f'Você digitou o numero {extenso[num]}')
