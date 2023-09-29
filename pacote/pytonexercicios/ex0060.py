#Crie um programa que leia um numero qualquer e mostre o seu fatorial
#Ex: 5! = 5x4x3x2x1 = 120

numero = int(input("Fatorial de: ") )

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)
print(count)


