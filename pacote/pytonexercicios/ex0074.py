#TUPLAS
#crie um programa que vai gerar cinco numero aleatorios e colocar em uma tupla
#mostre a listagem dos numeros, qual foi o menor e maior

import random
from random import randint
lista = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(lista)
print(max(lista))
print(min(lista))
print('Fim')
