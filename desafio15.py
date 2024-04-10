#aluguel de carro

dia = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos km você rodou com o carro?'))
preço_total = (60 * dia) + (0.15 * km)
print(f'O valor total ficou em R${preço_total:.2f}')
