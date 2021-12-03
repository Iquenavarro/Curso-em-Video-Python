#calculo do imc

peso = float(input('Digite seu peso (em kg): '))
altura = float(input('Digite a sua altura (em m): '))

imc = peso/(altura**2)

if  imc <= 10:
    print('Desnutrição Grau V seu IMC {}'.format(imc))
elif imc > 10 and imc <= 12.9:
    print('Desnutriçao Grau IV seu IMC {}'.format(imc))
elif imc >= 13 and imc <= 15.9:
    print('Desnutrição Grau III seu IMC {}'.format(imc))
elif imc >= 16 and imc <= 16.9:
    print('Desnutrição Grau II seu IMC {}'.format(imc))
elif imc >= 17 and imc <= 18.4:
    print('Desnutrição Grau I seu IMC {}'.format(imc))
elif imc >= 18.5 and imc <= 24.9:
    print('Peso normal seu IMC {}'.format(imc))
elif imc >= 25 and imc <= 29.9:
    print('Pré obesidade seu IMC {}'.format(imc))
elif imc >= 30 and imc <= 34.5:
    print('Obesidade grau I seu IMC {}'.format(imc))
elif imc >= 35 and imc <= 39.9:
    print('Obesidade grau II seu IMC {}'.format(imc))
else:
    print('Obesidade grau III seu IMC {}'.format(imc))
