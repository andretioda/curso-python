#FUNÇÕES - DEF

    #Interactive Help
    #docstrings
    #argumentos opcionais
'''
def somar(a, b, c = 0):
    s = a + b + c
    print(s)
somar(3 ,2 ,5)
somar(8, 4)
'''

    #escopo de variaveis
'''
def teste():
    x =8 #variavel local
    print(n) #global n
    print(x)

n = 2 #variavel global
print(n)
teste()
print(x)
'''

    #retorno de resultados
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(s)
    return s
r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)
print(r1, r2, r3)
