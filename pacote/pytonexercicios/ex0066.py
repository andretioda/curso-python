#Crie um programa que leia varios numeros inteiros e só pare quando for 999
#No final mostre quantos numeros foram digitados e qual foi a soma entre eles
#desconsiderar o flag

soma = cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma é de {soma}\n')

