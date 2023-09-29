#Crie um programa que pergunte a distancia de uma viagem em Km
#E calcule o preço da passagem.
#Sendo R$0,5/Km para viagens até 200Km e R$0,45/Km para viagens mais longas

pas = float(input('Qual a distancia em Km: '))
pas1 = pas * 0.5
pas2 = pas * 0.45

if pas >= 200:
    print('O preço da passgem ficou em {} '.format(pas1))
else:
    print('O preço da passgem ficou em {} '.format(pas2))


















