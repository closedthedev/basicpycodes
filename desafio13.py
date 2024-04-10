#reajuste de salário

salário = float(input('Digite seu salário:R$'))
aumento = float(input('Digite quantos % de aumento irá receber: '))
novo_salário = ((aumento / 100) * salário) + salário
print(f'O seu novo salário será R${novo_salário}')