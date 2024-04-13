#gerador de historia aleatória

import random

protagonistas = [' O herói' , ' O vilão' , ' O policial' , ' O ladrão']
ações = [' salvou' , ' matou' , ' prendeu' , ' roubou']
pessoa = [' um mendigo' , ' uma mulher' , ' um cachorro' , ' um homem']

print(random.choice(protagonistas) + random.choice(ações) + random.choice(pessoa))