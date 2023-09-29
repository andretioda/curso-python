#Crie um programa que leia duas notas e calcule a média
# <5 reprovado
# >7 aprovado
# 5>x<7 recuperação

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('Reprovado')
elif media > 7:
    print('Aprovado')
else:
    print('Recuperação')
























