#jogue par ou impar com o computador o jogo só é interrompido quando o usuário perder
import random
c = 1
pc = random.randint(0, 11)

escolha = str(input('Digite [P] para Par e [I] para ímpar: ')).strip().upper()[0]
while escolha not in "PpIi":
    escolha = str(input('Você só pode escolher entre Par ou Impar. Para Par, digite [P]. Para Ímpar, digite [I]')).strip().upper()[0]

while True:
    user = int(input('Escolha um numero: '))
    soma = pc + user
    if escolha == "P":
        print('Você escolheu PAR!')
        if soma % 2 != 0:
            print('Você perdeu, tente novamente')
            c += 1

        elif soma % 2 == 0:
            print('Você ganhou, parabéns!')
            c += 1
            print(f'O computador escolheu {pc} e você escolheu {user} foram necessárias {c} tentativas para ganhar.')

            break
    elif escolha == 'I':
        if soma % 2 == 0:
            print('Você perdeu, tente novamente')
            c += 1
        else:
            print('Você ganhou, parabéns')
            print(f'O computador escolheu {pc} e você escolheu {user} foram necessárias {c} tentativas para ganhar.')
            break

print('Programa encerrado')





