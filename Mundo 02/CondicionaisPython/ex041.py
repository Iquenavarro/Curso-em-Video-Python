#leia a data de nascimento e diga se a pessoa é mirim, juvenil
import datetime

atual = datetime.date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc

if  idade < 9:
    print('Aluno é mirim')
elif idade <= 14:
    print('Aluno é infantil')
elif idade <= 19:
    print('Aluno é junior')
elif idade <= 20:
    print('Aluno é senior')
else:
    print('Aluno é master')
