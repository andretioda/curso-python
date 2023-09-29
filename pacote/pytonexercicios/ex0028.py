#Crie um programa que faça o computador pensar em um numero inteiro entre 0 e 5
#e peça para o usuario tentar descobrir qual o numero
#o programa devera retornar se o usuario acertou ou não
import random

lista = [0,1,2,3,4,5]
nrandom = random.choice(lista)
nselect = int(input('Digite um numero de 0 a 5: '))

#print(nrandom)
print('O numero selecionado foi: {}'.format(nselect))

if nselect == nrandom:
    print('Parabens! Você acertou o número sorteado')
else:
    print('Você errou!')

print('O número sorteado foi: {}'.format(nrandom))










