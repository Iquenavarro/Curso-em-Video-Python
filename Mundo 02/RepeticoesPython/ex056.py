
mean = 0
counter = 0
adder = 0
add_age = 0
older = 0
name_older = ""

for i in range(1, 5):
    print('{} Pessoa'.format(i))
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip().upper()
    if sex == 'M':
        if age > older:
            older = age
            name_older = name
    elif sex == 'F':
        if age < 20:
            add_age += 1
    counter += 1
    adder += age
    mean = (adder / counter)

print('A media de idade do grupo é de {}.'.format(mean))
print('O nome do homem mais velho é {} e ele tem {} anos'.format(name_older, older))

if add_age == 0:
    print('Nenhuma mulher tem menos de 20 anos.')
elif add_age == 1:
    print('{} mulher tem menos de 20 anos.'.format(add_age))
elif add_age >= 2:
    print('{} mulheres tem menos de 20 anos.'.format(add_age))

