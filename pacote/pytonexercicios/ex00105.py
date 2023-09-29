#FUNÇÕES
#faça um programa que tenha uma função chamada notas()
#que receba varias notas de alunos e vai retornar um dicionario com as seguintes:
    #quantidade de notas
    #maior
    #menor
    #media geral
    #a situação (opcional)


def notas(*num, sit=False):
    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num)/len(num)
    if sit:
        if r['media'] > 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas (3.5, 5, 8, 9.75)
print(resp)

resp = notas (3.5, 5, 8, 9.75, sit=True)
print(resp)
