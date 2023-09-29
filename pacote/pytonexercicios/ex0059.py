#Crie um programa que leia dois valores e mostre um menu na tela:
#1 para somar
#2 para multiplicar
#3 maior
#4 novos numeros
#5 sair do programa

n = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
menu = 0

while menu != 5:
    print(('Lista de opções:\n'
                 '   [1] SOMAR\n'
                 '   [2] MULTIPLICAR\n'
                 '   [3] MAIOR\n'
                 '   [4] REINICIAR\n'
                 '   [5] SAIR\n'))
    menu = int(input('>>> Qual a sua escolha: '))
    if menu == 1:
        soma = n + n2
        print('A soma de {} e {} é {}'.format(n, n2, soma))

    elif menu == 2:
        mult = n * n2
        print('A multiplicação de {} e {} é {}'.format(n, n2, mult))

    elif menu == 3:
        maior = max(n, n2)
        print('O maior entre {} e {} é {}'.format(n, n2, maior))

    elif menu == 4:
        print('Informe os numeros novamente: ')
        n = float(input('Digite um numero: '))
        n2 = float(input('Digite outro numero: '))

    elif menu == 5:
        print('Finalizando...')
    else:
        print('Opção invalida')
print('Fim!')


