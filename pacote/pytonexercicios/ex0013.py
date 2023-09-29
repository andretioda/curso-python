#Faça um programa que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento

n = int(input('Digite salario atual: '))
n1 = n * (1+0.1500)

print('O salario atual é de {}. Com 15% de aumento será de {}'.format(n, n1))

