#FUNÇÕES
#faça um programa que tenha uma função maior()
#que receba varios parametros com valores inteiros
#ao final, o programa deverá dizer qual o maior deles

print('-' * 50)
def lista(*num):

    print('Analisando os valores passados...')
    for valor in num:
        print(valor, end=' ')

    print(f'Foram informados {len(num)} valores ao todo', end=' ')
    print(' ')
    print(f'O maior valor informado foi {max(num)}', end=' ')
    print(' ')
    print('-' * 50)
    if len(num) == 0:
        print(f'Foram informados {len(num)} valores ao todo')
        print(' ')
        print('O maior valor informado foi 0')


lista(2, 9, 4, 5, 7, 1)
lista(4, 7, 0)
lista(1, 2)
lista(6)
lista()
