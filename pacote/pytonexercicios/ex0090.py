#DICIONARIOS
#crie um programa que leia nome e media de um aluno
#ao final, mostre o conteudo da estrutura na tela

lista = {}
lista['nome'] = str(input('Nome: '))
lista['media'] = float(input(f'Media de {lista["nome"]}: '))

if lista['media'] >= 7: lista['situação'] = 'Aprovado'
elif 5 <= lista['media'] < 7: lista['situação'] = 'Recuperação'
else: lista['situação'] = 'Reprovado'

for k, v in lista.items():
    print(f'   {k} é igual a {v} ')

print('>>> Fim <<<')

