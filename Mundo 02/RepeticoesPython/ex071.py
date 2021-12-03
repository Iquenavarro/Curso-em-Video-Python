#simule o funcionamento de um caixa eletronico

saque = int(input('Qual valor você deseja sacar? '))

notas = [50, 20, 10, 1]

cedulas = []

counter = 0

while saque > 0:
        for val in notas:
            cedulas.append(saque // val)
            saque = saque % val
            print(f'{cedulas[counter]} notas de R$ {val}')
            counter += 1
counter = 0

print('Fim do Programa.')

