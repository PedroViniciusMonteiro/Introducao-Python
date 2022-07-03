def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador
if __name__ == '__main__':
    lista = ['tes', '2']
    print(contador_letras(lista))