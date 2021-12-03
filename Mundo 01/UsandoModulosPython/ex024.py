#Escreva se o nome da cidade comeca ou não com a palavra Santo

cidade = str(input('Digite o nome da sua cidade: '))

santo = cidade.lower().strip().split()
print(santo[0] == "santo")



