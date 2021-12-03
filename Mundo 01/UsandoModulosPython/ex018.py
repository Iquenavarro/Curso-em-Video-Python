#converte um angulo em radianos e calcula o seno, cosseno e a tangente
import math

ang = float(input('Digite um angulo em graus: '))

angrad = math.radians(ang)

seno = math.sin(angrad)
cosseno = math.cos(angrad)
tang = math.tan(angrad)

print('O seno do angulo vale {:.3f} \nO cosseno do angulo vale {:.3f} \nA tangente do angulo vale {:.3f}.'.format(seno, cosseno, tang))


