import os
#Manipulação de arquivos

cwd = os.getcwd()
print(cwd)
print(100*'-')

#lista os arquivos dentro da pasta
full_list = os.listdir(cwd)

#lista os aruqivos atraves do listcompreension
files_list = [i for i in full_list if os.path.isfile(i) and '.py' not in i]
types = list(set([i.split('.')[1] for i in files_list]))

#para cada tipo de arquivo criar um diretorio
for file_type in types:
    os.mkdir(file_type)

for file in files_list:
    from_path = os.path.join(cwd,file)
    to_path = os.path.join(cwd, file.split('.')[-1], file)

    os.replace(from_path, to_path)

