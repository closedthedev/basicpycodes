#dissecando variável

a = input('Digite qualquer coisa:')
print('É alfabético?', a.isalpha())
print('É numérico?' , a.isalnum())
print('Só tem espaços?', a.isspace())
print('É alfanumérico?', a.isalnum())
print('Está em maiúscula?', a.isupper())
print('Está em minúscula?', a.islower())
print('Está só com a primeira letra maiúscula?', a.istitle())