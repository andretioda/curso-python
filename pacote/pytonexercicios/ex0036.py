#Crie um programa para aprovar um emprestimo bancario
#Pergunte o valor, salario e anos de pagamento
#calcule o valor da prestação mensal, sabendo que nao pode exceder 30% do salario. Se nao o emprestimo é negado

emprestimo = float(input('Valor do empréstimo: '))
salario = float(input('Valor do salario: '))
anos = int(input('Prazo (anos): '))
prestaçao = float(emprestimo/anos)

if prestaçao <= (0.3*salario):
    print('Aprovado')
else:
    print('Reprovado')




















