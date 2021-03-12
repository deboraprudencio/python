# define e testa a função maximo(), que recebe três números e retorna o maior deles

def maximo (x, y, z):
    max = x
    if (y > x): max = y
    if (z > x): max = z

    return max

def test_1(): #s, m, l
    assert maximo (0,1,2) == 2

def test_2(): #m, s, l
    assert maximo (1,0,2) == 2

def test_3(): #l, m, s
    assert maximo (2,1,0) == 2

def test_4(): #m, l, s
    assert maximo (1,2,0) == 2

def test_5(): #l, s, m
    assert maximo (2,0,1) == 2

def test_6(): #with gaps
    assert maximo (1,3,5) == 5

def test_7(): #negative numbers
    assert maximo (-30,-400,-5) == -5

def test_8(): #positive and negative numbers
    assert maximo (300,-200,100) == 300

def test_9(): #equal numbers
    assert maximo (1,1,1) == 2

def test_10(): #equal numbers s,l,l
    assert maximo (1,2,2) == 2

def test_11(): #equal numbers l, s, l
    assert maximo (2,1,2) == 2

def test_12(): #equal numbers l, l, s
    assert maximo (2,2,1) == 1
