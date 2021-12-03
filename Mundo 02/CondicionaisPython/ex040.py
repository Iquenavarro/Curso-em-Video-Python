#leia duas notas e diga se o aluno está de recuperação, reprovou ou foi aprovado
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

media = (n1 + n2)/2

if media >= 7:
    print("Sua média é {} e você foi aprovado!".format(media))
elif media < 7 and media >= 5:
    print('Sua média foi {} e você está de recuperação!'.format(media))
else:
    print('Sua média foi {} e você está reprovado!'.format(media))
