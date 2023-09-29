#CORES NO TERMINAL

#STYLE
# 0 = nome
# 1 = bold
# 4 = underline
# 7 = negative

#TEXT
# 30 = branco
# 31 = vermelho
# 32 = verde
# 37 = cor padrão
#...

#BACK
# 40 = branco
# 41 = vermelho
# 42 = verde
# 47 = cor padrão
#...

print('\033[7;37;40m oi\033[m')

nome = 'andre'
print('oi, {}{}{}'.format('\033[4;37;40m', nome,'\033[m'))

