# define e testa a função soma_elementos
# a função recebe uma lista e devolve a soma de seus elementos

def soma_elementos(list):
    soma = 0
    for i in list:
        soma += i
    return soma

def test_1():
    assert soma_elementos([1, 2, 3, 4, 5]) == 15

def test_2():
    assert soma_elementos([7, 6, 12]) == 25

def test_3():
    assert soma_elementos([1000, 98, 30, 16]) == 1144