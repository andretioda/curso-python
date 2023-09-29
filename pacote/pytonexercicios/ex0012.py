#Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n = int(input('Digite preço atual: '))
n1 = n * (1-0.05)

print('O preço atual é de {}. Com 5% de desconto o preço será de {}'.format(n, n1))

