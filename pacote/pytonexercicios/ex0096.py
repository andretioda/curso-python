#FUNÇÕES
#faça um programa que tenha uma função chamada area()
#que receba dimensões de um terreno retangular (largura e comprimento) e mostre a area do terreno

def area(l, c):
    a = l * c
    print(f'A area de um terreno {l}x{c} é de {a} m².')


print('   Controle de Terrenos')
print('-' * 30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
