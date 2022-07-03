import shutil


def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()
def atualizar_arquivo(texto):
    arquivo = open("teste.txt", 'a')
    arquivo.write(texto)
    arquivo.close()
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas : sum([int (i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'teste.txt')
def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, './introducao-python')



if __name__ == '__main__':
    move_arquivo('teste.txt')
    #escrever_arquivo("Primeira linha")
    #atualizar_arquivo("\nSegunda linha")
    #ler_arquivo('teste.txt')