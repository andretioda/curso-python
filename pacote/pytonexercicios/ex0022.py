#Crie um programa que leia nome completo e apareça
#todas maiusculas
#todas minusculas
#quantas letras sem considerar espaço
#quantas letras tem o primeiro nome

nome = str(input('Qual o seu nome completo? '))
print('Nome completo: {}.'.format(nome))
print('Nome maiusculo: {}.'.format(nome.upper()))
print('Nome minusculo: {}.'.format(nome.lower()))
print('Nome tem: {} letras.'.format(len(nome)-nome.count(" ")))
print('Primeiro nome: {}.'.format(nome.split()[0]))




