#leia o sexo e idade de várias pessoas pergunte se o usuário quer continuar

somaidade = somahomens = somamulheres = 0

while True:
    idade = int(input('Digite uma idade: '))
    if idade >= 18:
        somaidade += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    while sexo not in 'MmFf':
        sexo = str(input('Digite somente [M ou F]: '))
    if sexo == 'M':
        somahomens += 1
    elif sexo == 'F':
        if idade >= 20:
            somamulheres += 1
    continuacao = str(input('Quer Continuar [S/N] ? ')).strip().upper()
    if continuacao == 'N':
        print(f'Pessoas com mais de 18 anos: {somaidade}')
        print(f'Homens Cadastrados: {somahomens}')
        print(f'Mulheres com mais de 20 anos: {somamulheres}')
        break


