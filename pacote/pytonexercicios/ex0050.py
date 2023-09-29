#Desenvolva um programa que leia 6 numeros inteiros
#e mostre apenas os pares. se valor digitado foi impar, desconsiderar

soma = 0
for c in range(1, 7, 1):
    n = int(input('Digite um número: '))
    if c % 2 == 0:
        soma += n
print('Soma dos numeros escolhidos é {}'.format(soma))
print(c)
