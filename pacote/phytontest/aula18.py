#LISTAS - VARIAVEL COMPOSTA
#SÃO MUTAVEIS
#LISTA COM LISTA

galera = [['joao', 19],['pedro', 25], ['maria', 23]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(p)

lista = []
dado = []
totmai = totmen = 0
for c in range(0 ,2):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    lista.append((dado[:]))
    dado.clear()
print(lista)
for p in lista:
    if p[1] >= 21:
        print(f'MAior: {p[0]}')
        totmai += 1
    else:
        print(f'MeNor: {p[0]}')
        totmen += 1
print(f'temos {totmai} maiores e {totmen} menores')
