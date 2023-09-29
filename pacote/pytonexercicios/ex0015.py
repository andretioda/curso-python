#Faça um programa de aluguel de carros - quanto pagar por dia alugado (60/dia e 0,15/km)

daluguel = int(input('Quantos dias alugados? '))
kaluguel = int(input('Quantos Km rodados? '))
taluguel = (daluguel * 60) + (kaluguel * 0.15)

print('O valor total foi de {}, sendo {} diarias e {} Km rodados.'.format(taluguel, daluguel, kaluguel))
