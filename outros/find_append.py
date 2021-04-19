def main (lista):
    '''
    Lê uma sequência de nomes e conta quantas vezes cada nome ocorre na sequência.
    '''
    def insereSeNovo (nome, lista):
        ''' (str, list) -> int
            modifica a lista, inserindo nome na lista.
            Retorna a posição de nome na lista
            Caso x não esteja na lista, insere x no final da lista e devolve none.
        '''
        for i in range(len(lista)):
            if lista[i] == nome: return i

        lista.append(nome)
        return None

    last = lista[len(lista) - 1]
    nome = ''

    while nome != last:
        nome = lista[0]
        n = 0
        while insereSeNovo(nome, lista) != None:
            lista.remove(nome)
            n += 1
        print(nome, "ocorre", n, "vezes")

main(["Neimar", "Messi", "Kaka", "Neimar", "Neimar", "Messi", "Zico"])
