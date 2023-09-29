#Crie um programa que leia nome completo e mostre primeiro e ultimo nome separadamente

nomecompleto= str(input('Digite nome completo: ')).strip()
nome = nomecompleto.split()

print(nomecompleto)
print(nome[0])
print(nome[len(nome)-1])












