#ERROS E EXCEÇÕES

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'ERRO: {erro.__class__}')
else:
    print(r)
finally:
    print('FINALIZANDO...')

