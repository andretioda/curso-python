#LISTAS
#faça um programa de cadastro de varios valores numerios e add em uma lista
#caso o numero ja exista, ele nao sera adicionado
#ao final, exibir todos os valores unicos, em ordem crescente

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    pe = ' '
    while pe not in 'SN':
       pe = str(input('Adicionar mais um valor? [S/N] ')).upper()
#    if pe == 'S':
#        lista.append(int(input('Digite um valor: ')))
#        str(input('Adicionar mais um valor? [S/N] ')).upper()
    if pe == 'N':
        print('Fim')
        break

lista.sort()
print(lista)

