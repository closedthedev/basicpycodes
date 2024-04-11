#calculando hipotenusa

import math

cateto_oposto = float(input('Qual o comprimento do cateto oposto?'))
cateto_adjacente = float(input('Qual o comprimento do cateto adjacente?'))
hipotenusa = math.hypot( cateto_oposto , cateto_adjacente)
print(f'A Hipotenusa vai medir {hipotenusa:.2f}')
