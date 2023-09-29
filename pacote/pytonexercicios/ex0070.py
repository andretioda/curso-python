# Crie um programa que leia o nome e preço de varios produtos - CADASTRO PRODUTO
# O programa deverá perguntar se o usuario quer continuar
# No final mostre:
# total gasto
# quantos produtos custam mais de R$1000
# qual é o nome do produto mais barato

cont1000 = tot = cont = menor = 0
menorp = ''
while True:
    nome = str(input('Digite nome do produto: '))
    preço = float(input('Digite preço do produto: '))
    cont += 1
    tot += preço
    if preço > 1000:
        cont1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        menorp = nome
    cad = ' '
    while cad not in 'SN':
        cad = str(input('Cadastrar novo produto: [S/N]: ')).upper()
    if cad == 'N':
        print('\n>>> Encerrando...\n')
        break
print(f'Total: {tot}')
print(f'Foram encontrados {cont1000} produtos custando mais de R$1.000')
print(menorp, menor)
