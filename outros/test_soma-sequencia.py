# teste de soma-sequencia.py

from soma_sequencia import max_soma

def test_0():
    assert max_soma([5, -2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1]) == 33 # Exemplo do exercício
    
def test_1():
    assert max_soma([5, -5, 6, -6, 7, -7, 8, -8]) == 8 # Todas as somas são iguais, maior soma é número individual
    
def test_2():
    assert max_soma([-5, -10, -8, -23, -100, -30, -60, -1]) == -1 # Maior soma é negativa e um único número
    
def test_3():
    assert max_soma([100, 200, -7, 8, -9, 10, -99, 100, -1]) == 303 # Maior soma é a primeira
    
def test_4():
    assert max_soma([100, -200, 7, 8, -30, 9, 10, -99, 9, 1, -40, -20, 9, 9, -3]) == 19 # Várias somas próximas distribuídas
    
def test_4():
    assert max_soma([6, -200, 7, -8, -9, 9, -99, 9, 1]) == 10 # Maior soma é a última
    
def test_5():
    assert max_soma([-5, -10, -8, -23, -100, -30, 5, -60, 0, -1]) == 5 # Maior soma é um único número
    
def test_6():
    assert max_soma([10, 20, -3, -2, -1, 7]) == 31 # Maior soma é a sequencia inteira