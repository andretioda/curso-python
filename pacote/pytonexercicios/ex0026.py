# Crie um programa que leia uma frase e diga
# quantas vezes aparece a letra A
# em que posição ela aparece a primeira vez
# em que posição ela aparece a ultima vez

frase = str(input(('Digite uma frase: '))).upper()

print(frase.count('A'))
print(frase.find('A')+1)
print(frase.rfind('A')+1)