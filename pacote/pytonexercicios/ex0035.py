#Crie um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou nao formar um triangulo

# Solicita os lados do triângulo
a = float(input("Lado a = "))  # Lado a
b = float(input("Lado b = "))  # Lado b
c = float(input("Lado c = "))  # Lado c

# Verifica se os lados formam um triângulo
if (a < b + c and b < a + c and c < a + b):
    # Verifica o tipo de triângulo
    if (a == b and b == c):
        print("\nTriângulo Equilátero.")
    elif (a == b or a == c or b == c):
        print("\nTriângulo Isósceles.")
    else:
        print("\nTriângulo Escaleno.")
else:
    print("\nOs lados não formam um triângulo!")

# Solicita para pressionar ENTER para sair
sair = input("\nDigite ENTER para sair...")



















