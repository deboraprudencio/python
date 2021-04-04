# define e testa a função maior_elemento
# a função recebe uma lista de números inteiros
# retorna seu elemento de maior valor 

def maior_elemento(list):
    max = list[0]
    for i in list:
        if (i > max): max = i
    return max

def test_1():
    assert maior_elemento([1, 2, 3, 4, 5]) == 5

def test_2():
    assert maior_elemento([10, 1000, 16, 1001, 18]) == 1001

def test_3():
    assert maior_elemento([8, 9, 9, 8, 9]) == 9

def test_4():
    assert maior_elemento([0, 0, 0, 0, 0]) == 0

def test_5():
    assert maior_elemento([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    
def test_6():
    assert maior_elemento([0, -10, -1000, -16, -1001, -18]) == 0
    
def test_7():
    assert maior_elemento([-10, -1000, -16, -1001, -18]) == -10