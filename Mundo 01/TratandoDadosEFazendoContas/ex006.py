#mostrar o dobro, o triplo e a raiz quadrada

num = int(input('Digite um número: '))

dobro = num*2
triplo = num*3
raiz = num**(1/2)

print('O dobro vale {}, o triplo vale {} e a raiz quadrada vale {:.3f}.'.format(dobro, triplo, raiz))
