#Faça um programa que leia um angulo,
# calcule e mostre o valor de seno, cosseno e tangente


from math import radians, sin, cos, tan

n = float(input('Digite o angulo: '))
s = sin(radians(n))
c = cos(radians(n))

t = tan(radians(n))

print('O valor digitado foi de {}. Resultado da hipotenusa de {:.2f}, {:.2f}, {:.2f}'.format(n, s, c, t))
