import os

opcao = 1
while opcao:
    print('')
    print('0. Para sair')
    print('1. Para soma')
    print('2. Para subtrair')
    print('3. Para Multiplicar')
    print('4. Para Dividir')
    print('')

    opcao = int(input('Informe uma opção de 0 a 4: '))
    if (opcao == 1):
        x = float(input('Entre com o primeiro valor: '))
        y = float(input('Entre com o segundo valor: '))
        print('')
        print('O valor da soma é: ', x + y)
        print('')

    if (opcao == 2):
        x = float(input('Entre com o primeiro valor: '))
        y = float(input('Entre com o segundo valor: '))
        print('')
        print('O valor da subtração é: ', x - y)
        print('')

    if (opcao == 3):
        x = float(input('Entre com o primeiro valor: '))
        y = float(input('Entre com o segundo valor: '))
        print('')
        print('O valor da multiplicação é: ', x * y)
        print('')

    if (opcao == 4):
        x = float(input('Entre com o primeiro valor: '))
        y = float(input('Entre com o segundo valor: '))
        if y == 0:
            print('A divisão não pode ser por Zero')
            print('')
        print('O valor da divisão é: ', x / y)

    if (opcao == 0):
        print('Voce saiu do programa')
        break