# Define e testa a função soma_matrizes(m1, m2)
# A função recebe 2 matrizes 
# Caso as matrizes tenham dimensões iguais, devolve uma matriz que represente sua soma
# Caso contrário, a função devolve False.

def soma_matrizes(m1, m2):
    matriz = []
    if (len(m2) == len(m1)):
        for i in range(len(m1)):
            coluna = []
            if (len(m2[i]) == len(m1[i])):
                for j in range(len(m1[i])):
                    coluna.append(m1[i][j] + m2[i][j])
                matriz.append(coluna)
            else: return False
        return matriz
    else: return False

def test_0():
    assert soma_matrizes([[1, 2, 3], [4, 5, 6]], [[2, 3, 4], [5, 6, 7]]) == [[3, 5, 7], [9, 11, 13]]

def test_1():
    m1 = [[1], [2], [3]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    assert soma_matrizes(m1, m2) == False