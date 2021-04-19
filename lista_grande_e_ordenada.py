from random import *
from sys import *

def lista_grande(n):
    return [randrange(- maxsize, maxsize) for i in range(n)]

def lista_quase_ordenada(n):
    lista = [i for i in range(n)]
    lista[n - 1] = 0
    return lista

def crescente(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]: return False
    return True

if __name__ == "__main__":
    print(lista_grande(10))
    print(lista_quase_ordenada(10))
    print(crescente([1, 2, 3, 4, 5]))
    print(crescente([1, 2, 3, 4, 1]))
    print(crescente(lista_quase_ordenada(10)))