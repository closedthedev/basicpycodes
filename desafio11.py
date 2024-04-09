#medidas

larg = float(input('Qual a largura da parede?'))
alt  = float(input('Qual a altura da parede?'))
área = larg * alt
tinta = área /2 
print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {área}m². Para pintar essa parede, você precisará de {tinta}l de tinta')