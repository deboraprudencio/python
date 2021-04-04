# Define e testa a função ssao_multiplicaveis()
# A função recebe duas matrizes e devolve True se forem multiplicaveis e False caso contrário

def sao_multiplicaveis(m1, m2):
    if len(m1[0]) == len(m2): return True
    else: return False

def test_0():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    assert sao_multiplicaveis(m1, m2) == False

def test_1():
    m1 = [[1], [2], [3]]
    m2 = [[1, 2, 3]]
    assert sao_multiplicaveis(m1, m2) == True