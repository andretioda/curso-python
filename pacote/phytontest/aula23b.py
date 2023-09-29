#ERROS E EXCEÇÕES

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError or TypeError):
    print('Problema com o tipo de dado')
except ZeroDivisionError:
    print('Nao é possivel dividir por zero')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados')
else:
    print(r)
finally:
    print('FINALIZANDO...')

