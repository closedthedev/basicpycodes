#criando um programa que leia o nome de uma pessoa e passe algumas informações interessantes
import string

nome = str(input('Digite seu nome completo: '))

nomema = nome.upper()
nomemi = nome.lower()
compnome = len(nome.replace(" ", ""))
nomeseparado = nome.split()
primeironome = nomeseparado[0]

print(f'Seu nome completo é {nome}, ele em maiúsculo fica {nomema}, ele em minúsculo fica {nomemi}, ele tem {compnome} caracteres e seu primeiro nome é {primeironome}')


