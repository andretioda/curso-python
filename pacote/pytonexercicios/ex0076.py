#TUPLAS
#desenvolva um programa que tenha uma tupla unica com nome e preço de produtos
#ao final, mostre lista de presços, organizando os dados em forma de tabular tabela

listagem = ('Lápis', 1.75,
          'Borracha', 2,
          'Caderno', 15.90)

print('-'*30)
print(f'{"LISTAGEM DE PRODUTOS":^30}')
print('-'*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<20}', end='')
    else:
        print(f'R$ {listagem[pos]:>5.2f}')
print('-'*30)