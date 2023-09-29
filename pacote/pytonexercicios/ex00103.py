#FUNÇÕES
#faça um programa que tenha uma função chamada ficha()
#que receba dois parametros: nome e qntde gols
#ao final, mostre a ficha do jogador mesmo que algum dado nao tenha sido informado corretamente

jogador = ' '
def ficha(jogador):
    return f'O jogador {nome} fez {gols} gols no campeonato.'


nome = str(input('Nome jogador: '))
gols = int(input('Numero de gols: '))
print(ficha(jogador))
