#LAÇOS DE REPETIÇÃO ITERAÇÃO - FOR

#for c in ranget (1:10)
#   passo
#pega

#for c in ranget (1:10)
#   passo
#   pula
#passo
#pega

for c in range(0, 6):
    print('Oi')
print('Fim')

for c in range(0, 6):
    print(c)
print('Fim')

for c in range(6, 0, -1):
    print(c)
print('Fim')

for c in range(0, 6, 2):
    print(c)
print('Fim')

s = 0
for c in range (0, 3):
    n = int(input('Digite um valor: '))
    s += n
print(s)
