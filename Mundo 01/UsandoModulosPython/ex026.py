#programa que leia uma frase e forneca informacoes sobre a frase

frase = str(input('Digite uma frase: ')).strip()

frasemin = frase.lower()
frasemin.count("a")

print('A frase tem {} letras A, a primeira aparece na {} posicao e a ultima aparece na {} posiçao.'.format(frasemin.count('a'), frasemin.find('a'), frasemin.rfind('a')))



