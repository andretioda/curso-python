#FUNÇÕES - DEF

    #Interactive Help
#help(print)

    #docstrings
def contador(i, f, p):
    """
    Faz a contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por André Tioda
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('Fim')


contador (2, 10, 2)

    #argumentos opcionais
    #escopo de variaveis
    #retorno de resultados


