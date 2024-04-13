#um simples programa perguntando se o nome da cidade que você nasceu começa com "Santo", se sim o programa vai mostrar true, se não vai mostrar falso.

import string


cidade = str(input('Digite o nome da cidade que você nasceu: '))
cidade.strip()

print(cidade[:5].upper == 'SANTO')

