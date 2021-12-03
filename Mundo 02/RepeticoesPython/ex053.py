# Após a sopa
# A sacada da casa
# A torre da derrota
# o lobo ama o bolo
# Anotaram a data da maratona

frase = str(input('Palindromo: ')).upper()

frase = "".join(frase.split(" "))

print('A palavra {} ao contrario é {} e '.format(frase, frase[::-1]), end="")

if frase == frase[::-1]:
    print('é um palindromo'. format(frase))
else:
    print('Não é um palindromo'.format(frase))