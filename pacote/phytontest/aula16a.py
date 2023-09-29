#TUPLAS - VARIAVEL COMPOSTA
#SÃO IMUTAVEIS

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche)
#print(lanche[1])
#print(lanche[2:])
#print(len(lanche))
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('>>>Fim\n')

#OU USANDO RANGE
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('>>>Fim\n')

#OU USANDO ENUMERATE
for pos, comida in enumerate(lanche):
    print(comida)
print('>>>Fim\n')

#MOSTRANDO EM ORDEM ALFABÉTICA
print(sorted(lanche))

