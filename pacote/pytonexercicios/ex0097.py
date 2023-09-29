#FUNÇÕES
#faça um programa que tenha uma função chamada escreva()
#que receba um texto qualquer como parametro
#e mostre uma mensagem com tamanho adaptavel

def escreva(msg):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)


escreva('Andre')
escreva('Andre Yuji')
escreva('Andre Yuji Tioda')
