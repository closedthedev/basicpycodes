#um programa que diga o primeiro e o último nome de uma pessoa

import string

nome = str(input('Digite o seu nome completo: '))
nomeseparado = nome.split()

primeironome = nomeseparado[0]
últimonome = nomeseparado[-1]

print(f'Seu nome completo é {nome}, seu primeiro nome é {primeironome} e seu último nome é {últimonome}')

