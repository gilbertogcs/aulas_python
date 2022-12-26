#trabalhando com listas

import os

lista_feira = ['Alface', 'Couve', 'Abobora','Pera','Maçã','Uva', 'Banana', 'Laranja', 'Limão']

#Percorrendo valores na lista com for
for feira in lista_feira:
    print(feira)

print('-----------------------------------------------')
print('')
lista_qualquer = ['Alface','Couve',200,'Olá Mundo']
print(lista_qualquer)


print('-----------------------------------------------')
print('')

#removendo elementos de uma lista

lista_feira.remove('Alface')
print(lista_feira)

print('-----------------------------------------------')
print('')
#removendo por posição
print(lista_feira)
print('------------------------------------------------')
print('')
print('Removendo por posições')

del lista_feira[1]
print(lista_feira)

print('------------------------------------------------')
print('removendo o ultimo elemento da lista')
del lista_feira[-1]
print(lista_feira)

#imprimir a posição da lista

os.system('cls')
print('Impressao da posição do item no comando for')

#O comando enumerate tras o numero de cada item dentro do comando for
for feira in enumerate(lista_feira):
    print(feira)
