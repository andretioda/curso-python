#Desenvolva um programa que leia o sexo de uma pessoa
#que só aceita M ou F
#Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper()
print('Fim')

