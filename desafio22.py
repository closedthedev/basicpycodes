#sorteando ordem da lista

import random

nome1 = str(input('Diga o nome de um aluno aleatório: '))
nome2 = str(input('Diga o nome de um aluno aleatório: '))
nome3 = str(input('Diga o nome de um aluno aleatório: '))
nome4 = str(input('Diga o nome de um aluno aleatório: '))
nome5 = str(input('Diga o nome de um aluno aleatório: '))

nomes = [nome1 , nome2 , nome3 , nome4 , nome5]
random.shuffle(nomes)

print(f'A ordem para apresentação do seminário será, respectivamente: {nomes} ')