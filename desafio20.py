#calculando seno, cosseno e tangente

import math

angulo = float(input('Digite o ângulo que queira saber o seno, cosseno e a tangente: '))
angulo1 = math.radians(angulo)

seno = math.sin(angulo1)
cosseno = math.cos(angulo1)
tangente = math.tan(angulo1)

print(f'O ângulo escolhido foi {angulo}, o seu seno é de {seno:.2f}, seu cosseno {cosseno:.2f} e sua tangente{tangente:.2f}')



