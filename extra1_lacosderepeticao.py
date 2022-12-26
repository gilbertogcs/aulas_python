import numpy as np
import pandas as pd
import os

#exemplo retirado do livro Guia pratico do python do básico ao avançado

n_tentativas = 10

print('Adivinha o numero entre 1  e 50, você tem {} chances!'.format(n_tentativas))

num_oculto = np.random.randint(0,50)
while n_tentativas>=0:
    n_tentativas = n_tentativas -1
    chute = int(input('Escolha um numero: \n'))
    if chute > num_oculto:
        print('O numero oculto é menor')
        print('Nº restante de tentativas = %d' % n_tentativas)
    elif chute < num_oculto:
        print('O Nº Oculto é maior!')
        print('Nº de tentativas = %d' % n_tentativas)
    else:
        print('Parabens, você acertou o Nº que é: %d' % num_oculto)
        break
if n_tentativas == 0:
    print('---------------------------------')
    print('Infelizmente suas tentativas acabaram')
    print('O numero oculto era %d '% num_oculto)
