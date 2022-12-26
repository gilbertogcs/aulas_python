import pandas as pd
import numpy as np
import os
import time

#fazendo a tabuada com numeros inteiros
#Fonte: https://guiatech.net/python-tabuada-de-um-numero-inteiro-qualquer/

#passo a passo
# 1 Receba o valor e armazene em uma variavel n
# 2 Multiplique  n, desde o zero até dez
# imprimir o resultado

n = int(input('Informe um valor para a tabuada: '))
print(30*'-')

i= 0

while i<=10:
    print('%2d x %2d = %2d' %(n, i,(n * i)))
    time.sleep(0.5)
    i += 1

sair = input('\nTecle enter para sair...')




