# FUNÇÕES
# faça um mini sistema que utilize o help do python
# com cor, colorindo fundo

c = ('\033[n',            # sem cores
     '\033[0;30;41m'     # vermelho
     )

def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP',1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATE LOGO...', 1)
