#curiosidade sobre alguns comandos
import random
from random import choice
import time

# lista_feira = ("Alface", "Couve", "Tomate", "Limão", "Mandioca", "Batata", "Manga", "Uva", "Abobora", "Cebola", "Melancia", "Mamão", "Melão", "Laranja", "Kiwi")
# lista_feira = list(lista_feira)
# print('Qtde ',len(lista_feira))
# #Enchendo o sacolão da feira
# sacolao = []
#
# while sacolao != "":
#     sacolao.append(random.choice(lista_feira))
#     time.sleep(0.8)
#     print('Adicionado ->{}'.format(sacolao))
#     if len(sacolao) == len(lista_feira):
#         break
# print()
# print('Fim da feira')
# print(180 * '=')
# print('A sacola da feira está com {}'.format(sacolao))

print()
print(70*'*' + ' Fazendo com outro exemplo ' + 70*'*')

lista_feira = (
"Alface", "Couve", "Tomate", "Limão", "Mandioca", "Batata", "Manga", "Uva", "Abobora", "Cebola", "Melancia", "Mamão",
"Melão", "Laranja", "Kiwi")
sacolao = []
lista_feira = list(lista_feira)

while True:
    if lista_feira == []:
        break
    else:
        item_escolhido = choice(lista_feira)
        sacolao.append(item_escolhido)
        indice = lista_feira.index(item_escolhido)
        lista_feira.pop(indice)
        print('Sacola com itens {}'.format(lista_feira))

print('sacoalão = ', sacolao)
