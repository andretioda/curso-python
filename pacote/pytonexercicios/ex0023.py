#Crie um programa que leia numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#unidade
#dezena
#centena
#milhar

numero = int(input('Digite um numero de 0 a 9999: '))

print('Numero digitado: {}'.format(numero))
print('Unidade: {}'.format(numero % 10))
unidade = int(numero % 10)
print('Dezena: {:.0f}'.format(((numero - unidade)/10) % 10))
dezena = int (((numero - unidade)/10) % 10)
print('Centena: {:.0f}'.format(((numero - dezena)/100) % 10))
centena = int(((numero - dezena)/100) % 10)
print('Milhar: {:.0f}'.format(((numero - centena)/1000)%10))


