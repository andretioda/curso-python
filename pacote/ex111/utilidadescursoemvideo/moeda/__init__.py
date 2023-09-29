def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(preço)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço + taxa/100)
    return res if formato is False else moeda(preço)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(preço)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(preço)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


