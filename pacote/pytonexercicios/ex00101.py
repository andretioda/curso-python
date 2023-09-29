#FUNÇÕES
#faça um programa que tenha uma função chamada voto()
#que vai receber parametros como: ano de nascimento
#retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório

from datetime import datetime
def voto(nasc):
    idade = datetime.now().year - nasc
    if idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATORIO'
    elif idade < 16:
        return f'Com {idade} anos: NAO VOTA'
    else:
        return f'Com {idade} anos: OPCIONAL'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

