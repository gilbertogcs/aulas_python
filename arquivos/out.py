import os
#fazendo o reverse do arquivo in.py

cwd = os.getcwd()
folder_list = [i for i in os.listdir(cwd) if os.path.isdir(i)]

#para cada pasta entra e retira o arquivo.
for folder in folder_list:
    path = os.path.join(cwd, folder)

    #verificar os aruqivos
    files = os.listdir(path)
    for file in files:
        from_path = os.path.join(path, file)
        to_path = os.path.join(cwd, file)
        os.replace(from_path, to_path)
    os.rmdir(path)