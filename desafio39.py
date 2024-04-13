#dividindo uma string em partes

frase = str(input('Digite uma frase: '))
num = int(input('Digite qual número da frase divida você quer: '))

frasedividida = frase.split()
fraseselecionada= frasedividida[num]

print(f'Você selecionou o número {num}, a frase dividida que condiz condiz com esse número é {fraseselecionada}')