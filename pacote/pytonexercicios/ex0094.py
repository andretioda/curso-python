#DICIONARIOS
#crie um programa que leie nome, sexo e idade de varias pessoas
#guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista
#ao final, mostre:
    #qutde pessoas cadastradas, média de idade, lista com mulheres e lista com idade cima da média

galera = []
pessoa = {}
cont = media = somaid = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = ' '
    cont += 1
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()
    pessoa['idade'] = int(input('Idade: '))
    somaid += pessoa['idade']
    media = somaid / cont
    galera.append(pessoa.copy())
    galera.clear()
    continua = str(input('Quer continuar [S/N]? ')).upper()
    if continua == 'N':
        print('Fim')
        break
print('-' * 30)
print(f'>>> Foram cadastradas {cont} pessoas.')
print(f'>>> A média de idade é de {media} anos.')
print(f'>>>As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ')
print(f'Lista de pessoas acima da média de idade ', end='')
for a in galera:
    if a['idade'] > media:
        print(f'{a["nome"]} ')
print('-' * 30)
