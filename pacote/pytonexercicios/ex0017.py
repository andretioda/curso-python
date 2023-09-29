#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo,
# calcule e mostre o comprimeto da hipotenusa
import math

n = float(input('Digite cateto oposto: '))
n1 = float(input('Digite cateto adjacente: '))
#n3 = (n ** 2 + n1 **2) ** (1/2)
n3 = math.hypot(n, n1)

print('O valor digitado foi de {}, o segundo de {}. Resultado da hipotenusa de {:.2f}'.format(n, n1, n3))
