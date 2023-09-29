#Melhore o ex0028
#computador pensa em um numero entre 0 e 10
#jogador responde até acertar
#ao final mostre a quantidade de tentativas

import random

lista = [0,1,2,3,4,5,6,7,8,9,10]
nrandom = random.choice(lista)
nselect = int(input('Digite um numero de 0 a 10: '))
print(nrandom)
tentativas = 1
while nselect != nrandom:
    nselect = int(input('Digite um numero de 0 a 10: '))
#   nrandom = random.choice(lista)
    print(nrandom)
    tentativas += 1
print('Acertou com {} tentativas'.format(tentativas))

