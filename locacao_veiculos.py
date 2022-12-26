#programa de locação de veiculos
import os #para efutuar a limpeza de tela

print('Bem vindo a locadora de carros!')
print('============')

carros= [
        ("Chevrolet Tracker", 120),
        ("Chevrolet Onix", 90),
        ("Chevrolet Spin", 150),
        ("Hyunday HB20", 85),
        ("Hyunday Tucson", 120),
        ("Fiat Uno", 60),
        ("Fiat Mobi", 70),
        ("Fiat Pulse", 130),
        ]

alugados =[]

#função para visualizar a lista de  carros

def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} /dia.".format(i, car[0], car[1]))



#Iniciando o programa
while True:
        os.system("cls")
        print('===============')
        print('Seja bem Vindo a locadora de carros')
        print('===============')
        print('0 - Mostrar Portifolio  | 1 - Alugar um Carro  |  2 - Devolver um carro')

        op = int(input())
        os.system("cls")
        if op == 0:
                mostrar_lista_de_carros(carros)

        elif op == 1:
                os.system("cls")
                mostrar_lista_de_carros(carros)
                print("==============")
                print("Escolha o codigo do carro: ")
                cod_car = int(input())
                print("Por quantos dias você deseja alugar o carro {}?".format(carros[cod_car][0]))
                dias = int(input())
                os.system("cls")
                print("Você escolheu {} por {} dias.".format(carros[cod_car][0], dias))
                #nessa operação esta sendo realizada a multiplicação de qtde de dias x o valor do carro
                print("O Aluguel totalizaria R$ {}. Deseja alugar?" .format(dias * carros[cod_car][1]))

                #pedindo a confirmação do usuário
                print("0 - Sim | 1 - Não")
                conf = int(input())

                #se a resposta do usuário for = 0 pegue o valor e passe para a lista de carros alugados com pop e append
                if conf ==0:
                        print("Parabéns você alugou o {} por {} dias.".format(carros[cod_car][0], dias))
                        print("")
                        print("O Total fica em R${}".format(dias * carros[cod_car][1]))
                        #comando pop vai extrair o valor na posição indicada e inserir dentro do append
                        alugados.append(carros.pop(cod_car))

        elif op == 2:
                #trabalhando a devolução dos carros
               if len(alugados) ==0:
                       print("Não há veiculos para serem devolvidos")
               else:
                       print("Segue a lista de carros, qual você deseja devolver: ")
                       mostrar_lista_de_carros(alugados)
                       print('')
                       print('Escolha o codigo do carro que deseja devolver: ')
                       mostrar_lista_de_carros(alugados)
                       print('')
                       print('Escolha o codigo do carro que deseja devolver:')
                       cod_car = int(input())
                       if conf ==0:
                               print('Obrigado por devolver o carro {}'.format(alugados[cod_car][0]))
                               carros.append(carros.pop(cod_car))

        print("")
        print('=============')
        print("0 Para Continuar  |  1 Para Sair")
        if float(input()) == 1:
                break
                

