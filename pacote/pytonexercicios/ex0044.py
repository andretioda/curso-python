#Elabore um programa que calcule o valor a ser pago, considerando preço e condição de pagamento
#a vista dinheiro/cheque 10% de desconto
#a vista no cartao 5% de desconto
#em até 2x 0%
#em 3x ou mais 20% de jurus

valor = float(input('Digite o valor: '))
tipo = str(input('Forma de pagamento: '))
prazo = int(input('Parcelas: '))
valordez = float(valor * 0.9)
valor5 = float(valor * 0.95)
valor020 = float(valor * 1.2)

if prazo == 1 and (tipo == 'dinheiro' or tipo == 'cheque'):
    print('Valor a ser pago com 10% de desconto {}'.format(valordez))
elif prazo == 1 and tipo == 'cartao':
    print('Valor a ser pago com 5% de desconto {}'.format(valor5))
elif prazo == 2:
    print('Valor a ser pago {}'.format(valor))
else:
    print('Valor a ser pago com 20% de jurus {}'.format(valor020))
