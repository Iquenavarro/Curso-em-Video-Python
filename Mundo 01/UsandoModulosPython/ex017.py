#leia o comprimento do cateto oposto e do adjacente e informe o valor da hipotenusa

import math

catop = float(input('Digite o valor do cateto oposto: '))

catad = float(input('Digite o valor do cateto adjacente: '))

hip = math.hypot(catad,catop)

print('O valor do cateto oposto é {}, o valor do catedo adjacente é {} e o valor da hipotenusa é {:.3f}.'.format(catop, catad, hip))



