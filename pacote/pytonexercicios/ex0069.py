#Crie um programa que leia a idade e o sexo de varias pessoas - CADASTRO PESSOA
#A cada cadastro perguntar se quer continuar
#No final mostre:
    #qtde pessoas > 18 anos
    #quantos homens
    #quantas mulheres < 20 anos

tot18 = totH = totM20 = 0
while True:
    print('-' * 50)
    idade = int(input('Qual a idade: '))
    sexo = ' '
    while sexo not in 'MH':
        sexo = str(input('Qual o sexo [H/M]: ')).upper()
    if idade > 18:
        tot18 += 1
    if sexo == "H":
        totH += 1
    if sexo == "M" and idade < 20:
        totM20 += 1
    print('-' * 50)
    p = ' '
    while p not in 'SN':
        p = str(input('>>> Realizar novo cadastro [S/N]? ')).upper()
    if p == "N":
        print('>>> Encerrando...')
        print('-' * 50)
        break
print(f'Existem {tot18} pessoas com mais de 18 anos.')
print(f'Existem {totH} pessoas do sexo masculino.')
print(f'Existem {totM20} mulheres com menos de 20 anos.')

