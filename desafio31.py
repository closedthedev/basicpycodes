#quantas vezes aparece a letra pedida

import string

frase = str(input('Digite uma frase: '))
letra = str(input('Qual letra você quer saber quantas vezes aparece na frase ?'))

letrapedida = frase.count(f'{letra}')

print(f'Você escolheu a letra {letra}, e ela aparece {letrapedida} vezes')

