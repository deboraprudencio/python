# Define e testa a função dimensoes(matriz)
# A função recebe uma matriz como parâmetro
# A função imprime as dimensões da matriz recebida, no formato iXj.

def dimensoes(matriz):
    print(str(len(matriz)) + "X" + str(len(matriz[0])))

def test_0():
    assert dimensoes([[1], [2], [3]]) == "3X1"

def test_1():
    assert dimensoes([[1, 2, 3], [4, 5, 6]]) == "2X3"