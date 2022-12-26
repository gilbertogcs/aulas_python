#lib os.path

import os
import time
#algumas funções do os.path

#agrupando nomes ao final de uma pasta

print('-----------------------------------------------------------------------------')
print('')
os_path_join = os.path.join(os.getcwd(), 'sua_nova_pasta')
print(os_path_join)
print('')
print('Ou pode ser feito desta forma')
os_path_outra_forma = os.getcwd() + '\pasta_outra_forma'
print(os_path_outra_forma)

print('------------------------------------------------------------------------------')
print('')

print('Retornando a ultima pasta dentro do caminho')
print('')
ultima_pasta = os.path.basename(os.getcwd())
print('A ultima pasta é ->',ultima_pasta)

print('------------------------------------------------------------------------------')
print('')

print('Quebrando as barras')
#esse comando pode servir para trocar as barras conforme o sistema operacional utilizado

quebra_barra = os.getcwd().split('/')
print(quebra_barra)

print('')
print('------------------------------------------------------------------------------')

pasta_atual = os.getcwd()
print(pasta_atual)
print('')

print('Tempo da ultima modificação')
#esse comando representa o tempo em segundos a partir da criação
ultima_modificacao = os.path.getmtime(pasta_atual)

print(ultima_modificacao)

print('')
print('Traduzindo o tempo em microsegundos para tempo')
print('')
#transformando em data
#nesse comando pode ser feito diversos outros comandos, tipo verificar qual foi a ultima modificação e etc.

from datetime import datetime
periodo = datetime.utcfromtimestamp(ultima_modificacao)
print('Criado em -> {}'.format(periodo))


print('')
print('---------------------------------------------------------------------------------------------------')

#verificando se é arquivo ou pasta
pasta = os.path.isfile(pasta_atual)
if pasta == False:
    print('Isso não é arquivo, é uma pasta -> {}'.format(pasta))
else:
    print('É um arquivo')

print('')
print('Fim')

print('----------------------------------------------------------------------------------------------------')
print('')

arquivo = os.path.isdir(pasta_atual)
if arquivo == False:
    x = 1
    while x<=5:
        print('Isso aqui é uma pasta -> {}' .format(pasta))
        time.sleep(1)
        x += 1
    print('Fim do Procedimento While')

else:
    print('Isso é um arquivo')

