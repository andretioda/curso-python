#FUNÇÕES
#faça um programa que tenha uma função chamada contador()
#que receba tres parametros: inicio, fim e passo e realize a contagem
#realizar tres contagens:
    #de 1 até 10, de 1 em 1
    #de 10 até 0, de 2 em se
    #uma contagem personalizada

from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1

    if p == 0:
        p =1

    print('-' * 20)
    print(f'Contagem de {i} até o {f} de {p} em {p}')
    sleep(1.0)

    if i< f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 20)
print('Agora é sua vez!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)

