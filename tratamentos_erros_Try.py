#tratamento de erros com try, exception e finally

x = int(input('Informe o primeiro Valor: '))
y = int(input('Informe o segundo valor: '))

op1 = x + y
op2 = x - y
op4 = x * y
op5 = x ** y

try:
    if y ==0:
        print('Algo de errado')

except ZeroDivisionError:
        print('Não pode ser dividido por 0')

except IndexError:
    print('Indice ')

print('A soma é {}'.format(op1))
print('A subtração é {}'.format(op2))
print('A Divisão é {}'.format(op3))
print('A multiplicação é {}'.format(op4))
print('A exponenciação é {}'.format(op5))

print('')
print('Fim')



