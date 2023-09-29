#Crie um programa que leia o ano de nascimento de um jovem e informe
#Se ele ainda vai se alistar
#Se é a hora de se alistar
#Se ja passou do tempo
#Mostrar tambem o tempo que falta ou que passou do prazo
from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
idade = 2023 - ano

if idade == 18:
    print('Alistar')
elif idade > 20:
    print('Ja passou a hora de se alistar')
else:
    print('Ainda vai se alistar')























