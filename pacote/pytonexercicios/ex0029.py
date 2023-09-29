#Crie um programa que leia a velocidade de um carro
#se >80Km/h, mostre mensagem de multado e calcule a multa (R$7 por km acima do limite)

vel = float(input('Qual a velocidade do carro: '))
vel2 = (vel - 80)
multa = (vel - 80)*7

if vel > 80:
    print('Você foi multado em {} por ultrapassar {} Km o limite de velocidade'.format(multa,vel2))
else:
    print('Tudo ok!')














