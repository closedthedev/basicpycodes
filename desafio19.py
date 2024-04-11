#embaralhando lista de nomes e sorteando

import random

nome1 = str(input('Diga o nome de um funcionário aleatório: '))
nome2 = str(input('Diga o nome de um funcionário aleatório: '))
nome3 = str(input('Diga o nome de um funcionário aleatório: '))
nome4 = str(input('Diga o nome de um funcionário aleatório: '))
nome5 = str(input('Diga o nome de um funcionário aleatório: '))

nomes = [nome1 , nome2 , nome3, nome4, nome5]
sorteio = random.shuffle(nomes)
nomesorteado = nomes[0]
print(f'{nomesorteado} foi sorteado(a) e ganhará uma viagem com tudo pago para a Itália.')