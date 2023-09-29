#DICIONARIOS
#crie um programa que gerencia o aproveitamento de um jogador de futebol
#o programa vai ler
    #nome e quantas partidas ele jogou
    #depois quantidade de gols feitos em cada partida
#ao final, guarde em um dicionario, incluindo total de gols

jogador = {}
partidas = []
jogador['nome'] = str(input('Nome: '))
tot = int(input(f'Nº partidas do {jogador["nome"]}: '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]

print('-' * 30)
print(jogador)
print('-' * 30)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i}, fez {v} gols.')
