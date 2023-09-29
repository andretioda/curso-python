#DICIONARIOS
#crie um programa que leia nome, ano de nascimento e carteira de trabalho
    #e cadastre-os (com idade) em um dicionario
    #se carteira for diferente de zero, o dicionario receberá tambem o ano de contratação e o salario
#calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar

from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - nasc
pessoa ['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salario: '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - datetime.now().year)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')

