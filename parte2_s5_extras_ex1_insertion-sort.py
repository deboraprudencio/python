from compara_desempenho import *
from lista_grande_e_ordenada import *

def insertion_sort(lista):
    '''insertion_sort(lista) --> lista
        Recebe uma lista com números inteiros como parâmetro
        Devolve esta lista em ordem crescente, utilizando o algoritmo insertion sort.
    '''

    for i in range(len(lista)):
        j = i
        while j > 0 and lista[j - 1] > lista[j]:
            lista[j], lista[j - 1] = lista[j - 1], lista[j]
            j -= 1
    return lista

def insertion_sort2(lista):
    '''insertion_sort(lista) --> lista
        Recebe uma lista com números inteiros como parâmetro
        Devolve esta lista em ordem crescente, utilizando o algoritmo insertion sort.
    '''

    for i in range(len(lista)):
        for j in range(i, 0, -1):
            if lista[j - 1] > lista[j]: lista[j], lista[j - 1] = lista[j - 1], lista[j]
            else: break
    return lista

if __name__ == "__main__":
    metodos = [insertion_sort, insertion_sort2]
    listas = [lista_grande(1000), lista_grande(2000), lista_quase_ordenada(1000), lista_quase_ordenada(2000)]

    print(Runtime(metodos, listas, crescente).run_all())