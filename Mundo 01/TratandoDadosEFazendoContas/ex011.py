#leia a largura e a altura da parede e determine a área e quantos litros de tinta serão necessarios

comp = float(input('Digite o comprimento (em metros): '))
altura = float(input('Digite a altura (em metros): '))

area = comp * altura
litros = (area / 2)

print('A área da parede é {} m².\nSerão necessários {} litros.'.format(area, litros))
