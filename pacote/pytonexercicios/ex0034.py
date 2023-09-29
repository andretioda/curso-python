#Crie um programa que pergunte o salario
#para salarios > 1.250 calcule 10% de aumento
#para salarios <=, o aumento é de 15%

salario = float(input('Salario: '))

if salario > 1250:
    salario1 = salario * 1.1
    print('Seu novo salário é de {}'.format(salario1))
else:
    salario2 = salario * 1.15
    print('Seu novo salário é de {}'.format(salario2))





















