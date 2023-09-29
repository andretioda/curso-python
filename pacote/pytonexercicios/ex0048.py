#Crie um programa que calcule todos os numeros impares que são múltiplo de três no intervalo de 1 a 500

soma = 0
cont = 0
for c in range (1,501,2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

