def bubble_sort(lista):
    '''bubble_sort(lista) --> lista
        Recebe uma lista com números inteiros como parâmetro
        Devolve esta lista em ordem crescente, utilizando o algoritmo bubble sort.
        Imprime o estado atual da lista toda vez que faz uma alteração em seus elementos.
    '''

    reordenou = False

    for i in range(len(lista) - 1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)
                reordenou = True
        if not reordenou: return lista
    return lista

def test_bubble(resultado):
    listas = [[1, 1.5, 3, 4.5, 0, 5, 11], [5, -40, 0, 2000, -30, 200, -25], [45, 3000, 250.5, -4000, 300, 100, -6000], [5, 1, 4, 2]]
    resultado_esperado = [[0, 1, 1.5, 3, 4.5, 5, 11], [-40, -30, -25, 0, 5, 200, 2000], [-6000, -4000, 45, 100, 250.5, 300, 3000], [1, 2, 4, 5]]

    for l in range(len(listas)):
        if bubble_sort(listas[l]) == resultado_esperado[l]: print("passou no teste", l)
        else: print("falhou no teste", l)

if __name__ == "__main__":
    test()