#LISTAS
#faça um programa de cadastro de nome e peso e guarde em uma lista
#ao final, mostre: qntde pessoas cadastradas, lista com as pessoas mais pesadas e outra com mais leves

lista = []
dado = []
mai = men = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(lista) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    lista.append(dado[:])
    dado.clear()
    continua = str(input('Quer continuar [S/N]? ')).upper()
    if continua in 'N':
        break
#print(lista)
print(f'>>> Ao todo foram cadastradas {len(lista)} pessoas.')
print(f'>>>O maior peso encontrado foi: {mai} Kg')
for p in lista:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print()
print(f'>>>O menor peso encotrado foi: {men} Kg')
for p in lista:
    if p[1] == men:
        print(f'{p[0]} ', end='')
