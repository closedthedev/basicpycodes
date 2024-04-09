#descontos
valor = float(input('Qual o valor original? '))
desconto = float(input('Qual a porcentagem de desconto?'))
valor_desconto = (desconto/ 100) * valor
valor_final =  valor - valor_desconto
print(f'O valor final, com desconto, ficou {valor_final} ')