#DICIONARIOS
#continuação do ex0093
#aprimore para que funcione com varios jogadores, incluindo sistema de visualização detalhada do aproveitamento
galera = []
partidas = []
jogador = {}
while True:
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Nº partidas do {jogador["nome"]}: '))
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    galera.append(jogador.copy())
    partidas.clear()
    continua = str(input('Quer continuar [S/N]? ')).upper()
    if continua == 'N':
        print('Fim')
        break

print('-' * 30)
print(galera)
print('-' * 30)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 30)
for k, v in enumerate(galera):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 30)

while True:
    opc = int(input('Selecionar jogador pelo No: '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc >= len(galera):
        print(f'ERRO!')
    else:
        print(f'---Levantamento do jogador: {galera[opc]["nome"]}---')
        for i, g, in enumerate(galera[opc]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-' * 30)
print('Fim')
