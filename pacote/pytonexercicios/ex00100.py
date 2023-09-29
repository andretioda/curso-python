#FUNÇÕES
#faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia e somaPar
#a primeira função vai sortear 5 numeros e add dentro da lista
#a segunda função vai mostrar a soma entre todos os pares sorteados


import random
from random import randint

def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(n, end=' ')
    print(' ')

def somaPar(lista):
    print(f'Somando os valores pares, temos: ')
    soma = 0
    for valor in lista:
        if valor % 2 ==0:
            soma += valor
    print(soma, end=' ')
    print(' ')


numeros = []
sorteia(numeros)
somaPar(numeros)
