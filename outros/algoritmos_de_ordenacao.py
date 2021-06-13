from compara_desempenho import *
from random import *
from sys import *

def insercao(seq):
    ''' (list) -> list
        ordena a lista seq usando o algoritmo de insercao
        '''
    for i in range(len(seq)):
        j = i
        while j > 0 and seq[j - 1] > seq[j]:
            seq[j], seq[j - 1] = seq[j - 1], seq[j]
            j -= 1
    return seq

def selecao(seq):
    ''' (list) -> list
        ordena a lista seq usando o algoritmo de selecao
        '''
    for i in range(len(seq)):
        menor = i
        for j in range(i + 1, len(seq)):
            if seq[j] < seq[menor]: menor = j
        seq[i], seq[menor] = seq[menor], seq[i]
    return seq

def bolha(seq):
    ''' (list) -> list
        ordena a lista seq usando o algoritmo de bolha
        '''
    trocou = True
    while trocou == True:
        for i in range(len(seq) - 1):
            trocou = False
            if seq[i + 1] < seq[i]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                trocou = True
    return seq

def testes():
    def lista_aleatoria(n):
        return [randrange(- maxsize, maxsize) for i in range(n)]

    def lista_quase_ordenada(n):
        lista = [i for i in range(n)]
        lista[n - 1] = 0
        return lista

    def lista_invertida(n):
        lista = [n - i for i in range(n)]
        return lista

    def lista_muito_repetida(n):
        elementos = [randrange(- maxsize, maxsize) for i in range(n//4)]
        lista = [elementos[randrange(0, len(elementos))] for i in range(n)]
        return lista

    def crescente(seq):
        ''' (list) -> bool
        retorna True se seq esta em ordem crescente
        e False caso contrario
        '''
        for i in range(len(seq) - 1):
            if seq[i + 1] < seq[i]: return False
        return True

    def teste_crescente():
        listas = [[1, 2, 3], [1, 1, 1], [-1, -2, -3], [-3, -2, -1], [1, 3, 1], 
            [3, 1, 2], [1.1, 1.2, 1.3], ["a", "b", "c"], ["c", "b", "a"]]
        for seq in listas: print(seq, crescente(seq))
    
    def teste_listas():
        print(lista_aleatoria(10))
        print(lista_invertida(10))
        print(lista_quase_ordenada(10))
        print(lista_muito_repetida(10))
    
    def teste_algoritmos():
        metodos = [insercao, selecao, bolha]
        listas = [lista_aleatoria(7500), lista_invertida(7500), lista_quase_ordenada(7500), lista_muito_repetida(7500)]
        print(Runtime(metodos, listas, crescente).run_all())
    
    teste_crescente()
    teste_listas()
    teste_algoritmos()

if __name__ == "__main__": testes()