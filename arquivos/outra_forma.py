import os
#fonte: https://youtu.be/5vdEb_pitfc

#Criando as listas do tipo dos arquivos.

audio_ext = ['.mp3', '.wav']
videos_ext = ['.mp4', '.mov', '.avi']
imagens_ext = ['.jpg', 'jpeg','.png']
documentos_ext = ['.txt','.csv','xlsx','.xls','.pdf','.doc', '.docx']
compactados_ext = ['.zip','.rar','.7z']


def pegar_extensao(nome):
    index = nome.rfinde('.')
    #pega nome do arquivo a partir do final
    return nome[index:]

def organizar(diretorio):
    #criar as pastas
    AUDIO_DIR = os.path.join(diretorio, "audios")
    IMAGENS_DIR = os.path.join(diretorio,"imagens")
    DOC_DIR = os.path.join(diretorio,"documentos")
    VIDEOS_DIR = os.path.join(diretorio, "videos")
    DIR_ZIP = os.path.join(diretorio, "zipados")
    OUTROS_DIR = os.path.join(diretorio,"outros")

    #criando as pastas e verificando se existe
    if not os.path.isdir(AUDIO_DIR):
        os.mkdir(AUDIO_DIR)

    if not os.path.isdir():
        os.mkdir(IMAGENS_DIR)

    if not os.path.isdir(DOC_DIR):
        os.mkdir(DOC_DIR)

    if not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)

    if not os.path.isdir(OUTROS_DIR):
        os.mkdir(OUTROS_DIR)

    if not os.path.isdir(DIR_ZIP):
        os.mkdir(DIR_ZIP)


    nomes_arquivos = os.listdir(diretorio)
    nova_pasta = ''
    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            extensao = str.lower(pegar_extensao(arquivo))
            if extensao in audio_ext:
                nova_pasta = AUDIO_DIR
            elif extensao in videos_ext:
                nova_pasta = VIDEOS_DIR
            elif extensao in imagens_ext:
                nova_pasta = IMAGENS_DIR
            elif extensao in documentos_ext:
                nova_pasta = DOC_DIR
            elif extensao in compactados_ext:
                nova_pasta = DIR_ZIP
            else:
                nova_pasta = OUTROS_DIR

            #mover os arquivos
            velho = os.path.join(diretorio, arquivo)
            novo = os.path.join(nova_pasta, arquivo)
            os.rename(velho, novo)
            print('Moveu: '.velho, '-> ', novo)

if __name__ == '__main__':
    organizar('c:\\Users\\Gilberto\\Downloads\\')