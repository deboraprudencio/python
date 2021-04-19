def busca(lista, elemento):
    '''busca(lista, elemento) --> index
        Busca um determinado elemento em uma lista ordenada.
        Devolve o índice do elemento ou False se ele não existir na lista.
        Utiliza o algoritmo de busca binária.
        Imprime cada um dos índices testados pelo algoritmo.
    '''

    inicio, fim = 0, len(lista) - 1

    while inicio <= fim:
        m = inicio + ((fim - inicio) // 2)
        print(m)
        if lista[m] == elemento: return m
        elif lista[m] > elemento: fim = m - 1
        elif lista[m] < elemento: inicio = m + 1
    return False

def test():
    listas = [[1, 2, 3, 4, 5], [-30, -20, 0, 70, 200], [-4000, 90, 100, 200, 300]]
    elementos = [[0, 1, 1.5, 3, 4.5, 5, 11], [-40, -30, -25, 0, 5, 200, 2000], [-6000, -4000, 45, 100, 250.5, 300, 3000]]

    for l in range(len(listas)):
        resultados = []
        for e in range(len(elementos[l])):
            resultados.append(busca(listas[l], elementos[l][e]))
        if resultados == [False, 0, False, 2, False, 4, False]: print("passou no teste", l)
        else: print("falhou no teste", l)

    print("r =", busca(['a', 'e', 'i'], 'e'))
    # 1
    # deve devolver => 1

    print("r =", busca([1, 2, 3, 4, 5], 6))
    # 2
    # 3
    # 4
    # deve devolver => False

    print("r =", busca([1, 2, 3, 4, 5, 6], 4))
    # 2
    # 4
    # 3
    # # deve devolver => 3

if __name__ == "__main__":
    test()