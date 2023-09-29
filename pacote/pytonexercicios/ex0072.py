#TUPLAS
#crie um programa que tenha uma tupla totalmente preenchida de zero até vinte
#o programa devera ler um numero pelo teclado e mostra-lo por extenso

lista = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco')
lista2 = (0, 1, 2, 3, 4, 5)
n = ''
while n not in lista2:
    n = int(input('Digite um numero: '))
print(lista[n])

