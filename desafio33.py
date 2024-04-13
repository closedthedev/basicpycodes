#substituindo uma palavra por outra

import string

frase = str(input('Digite uma frase: '))
letra1 = str(input('Qual palavra você quer tirar? '))
letra2 = str(input('Qual palavra você quer que entre no lugar dela? '))

nova_frase = frase.replace(letra1 , letra2)

print(nova_frase)