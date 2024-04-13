#um programa que pergunta qual seu nome, se você tiver o sobrenome Ferreira, vai responder true. caso contrário, responderá false.
import string


nome = str(input('Digite o seu nome completo: '))
nome.strip()
nome.upper

print('Ferreira' in nome)
