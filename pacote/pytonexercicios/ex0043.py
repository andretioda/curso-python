#Desenvolva uma logica que leia o peso e altura, calculando o IMC
#<18.5 abaixo do peso
#18.5>x<25 peso ideal
#25<x<30 sobrepeso
#30<x<40 obesidade
#>40 obesidade mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura*altura)

print('IMC: {:.2f}'.format(imc))

if imc <= 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade moibida')