n = input('Digite algo: ')

print('O tipo primitivo desse valor é', type(n))
print('Só tem espaços? ', n.isspace())
print('É alfabético?', n.isalpha())
print('É alfanumérico? ', n.isalnum())
print('Está em maisculo? ', n.isupper())
print('Esta em minusculo? ', n.islower())
print('Está capitalizado?', n.istitle())
