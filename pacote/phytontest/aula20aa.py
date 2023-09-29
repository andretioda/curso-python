#FUNÇÕES - DEF
'''
a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)
'''

'''
def soma(a ,b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma (2, 1)
print(' ')

def contador (*num):
    for valor in num:
        print(valor, end='')
    print('Fim')


contador(2 , 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9]
dobra(valores)
print(valores)
