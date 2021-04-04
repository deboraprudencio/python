#arquivo de testes do semana9_desafio_temp-max-e-min.py

from semana9_desafio_temp_maxmin import temperaturas_extremas 

def test_1():
    assert temperaturas_extremas([1, 2, 3, 4, 5]) == [5, 1]

def test_2():
    assert temperaturas_extremas([10, 1000, 16, 1001, 18]) == [1001, 10]

def test_3():
    assert temperaturas_extremas([8, 9, 9, 8, 9]) == [9, 8]

def test_4():
    assert temperaturas_extremas([0, 0, 0, 0, 0]) == [0, 0]

def test_5():
    assert temperaturas_extremas([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1]
    
def test_6():
    assert temperaturas_extremas([0, -10, -1000, -16, -1001, -18]) == [0, -1001]
    
def test_7():
    assert temperaturas_extremas([-10, -1000, -16, -1001, -18]) == [-10, -1001]