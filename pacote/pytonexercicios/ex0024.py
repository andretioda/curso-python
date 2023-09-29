#Crie um programa que leia nome da cidade e diga se ela começa ou não com o nome Santo

nomecidade = input('Digite nome de uma cidade: ')
palavra = "Santo"

if palavra not in nomecidade:
    print("A cidade não tem " + palavra)
else:
    print("A Cidade tem " + palavra)








