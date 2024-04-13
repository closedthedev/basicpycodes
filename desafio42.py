#pegando um número e dizendo qual é a unidade, dezena, centena e milhar

import random


numero = int(input('Digite um número de 1 a 9999  '))

milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = (numero % 100) // 10
unidade = numero % 10

print(f'Você escolheu o número {numero}. O milhar dele é {milhar}, a centena dele é {centena}, a dezena dele é {dezena} e a unidade dele é{unidade}.')




