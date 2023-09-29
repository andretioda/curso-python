#Crie um programa que jogue jokenpo com voce
import random

escolha = str(input('papel, tesoura ou pedra: '))
lista = ['papel', 'tesoura', 'pedra']
computador = str(random.choice(lista))

print('Escolha do oponente: '.format(computador))

if escolha == computador:
    print('Empatou')
elif escolha == 'papel' and computador == 'tesoura':
    print('Você perdeu')
elif escolha == 'papel' and computador == 'pedra':
    print('Você ganhou')
elif escolha == 'tesoura' and computador == 'papel':
    print('Você ganhou')
elif escolha == 'tesoura' and computador == 'pedra':
    print('Você perdeu')
elif escolha == 'pedra' and computador == 'papel':
    print('Você perdeu')
elif escolha == 'pedra' and computador == 'tesoura':
    print('Você ganhou')
else:
    print('Digite novamente...')