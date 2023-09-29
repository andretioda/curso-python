#TUPLAS
#desenvolva um programa que leia e 4 valores e guarda-os em uma tupla
#no final, mostre
    #quantas vezes aparece o valor 9
    #posição do primeiro valor 3
    #quais os numeros pares

lista = (
    int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),
    int(input('Digite um numero: ')))
print(lista)
print(lista.count(9))
print(lista.index(3)+1)
for n in lista:
    if n % 2 ==0:
        print(n)
