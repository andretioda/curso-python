#LISTAS
#faça um programa que leia 5 valores numericos e guarde-os em uma lista
#no final, mostre qual o maio e o menor e suas respectivas posições na lista
from operator import index

lista = []
for cont in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

ma = max(lista)
map = lista.index(max(lista))
mi = min(lista)
mip = lista.index(min(lista))

print('O maior valor é o {ma} na posição {map}.')
print('O menor valor é o {mi} na posição {mip}.')
