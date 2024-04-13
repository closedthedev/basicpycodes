#um programa que busque uma letra específica, posição da primeira e última aparição dela.

import string

frase = str(input('Digite uma frase: '))
letra = str(input('Digite qual letra da frase queira os dados especificados: '))

quantasletras = frase.count(letra)

primeira_pos = frase.find(letra)
segunda_pos = frase.rfind(letra)

print(f'Você digitou a frase: "{frase}". Escolheu a letra "{letra}". A primeira vez que a letra "{letra}" foi na posição {primeira_pos}, e a última vez foi na posição {segunda_pos}')

