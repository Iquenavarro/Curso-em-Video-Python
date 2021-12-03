# Leia o sexo de uma pessoa e so aceite caso seja M ou F. Caso esteja errado faça a digitação

sex = str(input('Digite M ou F: ')).strip().upper()[0]

while sex not in "MfFf":
    sex = str(input("O arrombado, digita M ou F: ")).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sex))

