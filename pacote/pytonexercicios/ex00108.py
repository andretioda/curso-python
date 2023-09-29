#FUNÇÕES
#formatação moeda

def aumentar(preço=0, taxa=0):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço=0, taxa=0):
    res = preço - (preço + taxa/100)
    return res


def dobro(preço=0):
    res = preço * 2
    return res


def metade(preço=0):
    res = preço / 2
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


p = float(input('Digite o preço (R$): '))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando 10%, temos: {moeda(aumentar(p, 10))}')
