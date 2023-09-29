#Refaça o ex009, mostrando a tabuada de um numero escolhido

for c in range (0,1):
    n = int(input('Digite um valor: '))
    t = n * 1, n * 2, n * 3, n * 4, n * 5, n * 6, n * 7, n * 8, n * 9, n * 10
print(t)

n = int(input('Digite um valor: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n * c))

