#Crie um programa que leia o ano de nascimento
#até 9 anos: mirim
#14 anos: infantil
#19 anos: junior
#20anos: senior
#>20: mastar

ano = int(input('Digite seu ano de nascimento: '))
idade = 2023 - ano

print('A sua idade é: {}'.format(idade))
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <=20:
    print('Senior')
else:
    print('Master')
