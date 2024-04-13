#localizando uma sequencia de letras

import string

frase = str(input('Digite uma frase: '))
letras = str(input('Qual sequencia de letras você quer localizar? '))

letrapedida = frase.find(f'{letras}')

print(f'Você escolheu as letras {letras}, e elas aparecem na posição {letrapedida}')