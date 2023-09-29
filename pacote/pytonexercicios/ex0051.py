#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.

p = int(input('Digite primeiro termo: '))
r = int(input('Digite razão: '))
d = p + (10-1) * r
for c in range(p, d, r):
    print('{}'.format(c), end='->')
print('Fim')