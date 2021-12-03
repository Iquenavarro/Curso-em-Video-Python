from datetime import datetime

nascimento = int(input('Qual o seu ano de nascimento? '))

atual = datetime.now().year
alistamento = atual - nascimento

if  alistamento > 18:
    print('Já passou da hora de se alistar! O país precisa de você!')
elif alistamento == 18:
    print('Esta no ano de se alistar, faça sua parte!')
else:
    print('Ainda faltam {} anos para o seu alistamento.'.format(18-alistamento))

