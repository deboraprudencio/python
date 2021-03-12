# define e testa a função maximo(), que recebe dois números e retorna o maior deles

def maximo (x, y):
    if (x > y): return x
    else: return y

def test_1():
    assert maximo (0,1) == 1

def test_2():
    assert maximo (1,2) == 2

def test_3():
    assert maximo (3,0) == 3

def test_4():
    assert maximo (-10,10) == 10

def test_5():
    assert maximo (-100,200) == 200

def test_6():
    assert maximo (3,4) == 4

def test_7():
    assert maximo (0,-1) == 0
