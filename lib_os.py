#trabalhando a lib os


import os

print('')
print('------------------------------------------------------------------------------------')

print('Mostrar o caminho atual')
caminho = os.getcwd() #mostra o caminho atual
print(caminho)

print('')
print('------------------------------------------------------------------------------------')

print('listar todos os arquivo na pasta atual')
#listar os arquivos dentro da pasta atual
lista_arquivos = os.listdir()
print(lista_arquivos)
print('')
print('-------------------------------------------------------------------------------------')

print('listar todos os arquivo na pasta anterior ')
#listar os arquivos dentro da pasta anterior
lista_arquivos_pasta_anterior = os.listdir('/Projeto_Py/Asimov_academy')
print(lista_arquivos_pasta_anterior)
print('')
print('--------------------------------------------------------------------------------------')

print('Trocando o diretorio')

diretorio_atual = os.getcwd()
print('O diretorio atual é ->',diretorio_atual)
print('')
diretorio_anterior = os.chdir(diretorio_atual)
print('O diretorio anterior é ->',diretorio_anterior)
print('')
print('--------------------------------------------------------------------------------------')

print('Criando Pasta')
#os.mkdir('Pasta_criada_via_lib')
print('')
print('Listando os arquivos e pasta', lista_arquivos)

print('')
print('--------------------------------------------------------------------------------------')

print('Renomeando e movendo arquivos com o Rename')
print('')
print('------>',lista_arquivos)
#os.rename('testes99.txt','teste10.txt')
#neste comando movimentei a pasta 'Pasta_criada_via_lib' para dentro da pasta 'Pasta_criada_via_lib999
#os.rename('Pasta_criada_via_lib','Pasta_criada_via_lib999/Pasta_criada_via_lib')
print('======>',lista_arquivos)

print('')
print('--------------------------------------------------------------------------------------')
print('Apagando arquivos')
#os.remove('teste10.txt')
print('')
print('Apagando uma pasta')
print('')
#nesse comando apaguei a pasta que estava dentro de 'Pasta_criada_via_lib999
os.rmdir('Pasta_criada_via_lib999/Pasta_criada_via_lib')
