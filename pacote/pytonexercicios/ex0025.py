#Crie um programa que leia nome de uma pessoa e diga se ela tem Silva no nome

nome= input('Digite nome: ')
palavra = "Silva"

if palavra not in nome:
    print("O nome não tem " + palavra)
else:
    print("O nome tem " + palavra)











