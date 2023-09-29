#LISTAS
#crie um programa que leie nome e duas notas de varios alunos e guarde em lista composta
#ao final, mostre um boletim contendo a média de cada aluno
#e permita que o usuario possa mostrar as notas de cada aluno individualmente

lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, nota1, nota2, media])
    continua = str(input('Quer continuar [S/N]? ')).upper()
    if continua == 'N':
        break
print(' ')
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    print(' ')
while True:
    opc = int(input('Selecionar aluno pelo No: '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]} e {lista[opc][2]} ')
print(' ')
print('Fim')

