#DICIONARIOS - VARIAVEL COMPOSTA

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(' ')
for k, v in pessoas.items():
    print(f'{k} = {v}')
print(' ')
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
print(' ')
