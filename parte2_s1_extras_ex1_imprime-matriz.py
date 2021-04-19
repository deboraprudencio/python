# Define a função imprime_matriz
# A função recebe uma matriz e a imprime linha por linha

def imprime_matriz(matriz):
    for linha in matriz:
        for i in range(len(linha)):
            if (i != len(linha) - 1): print(linha[i], end = " ")
            else: print(linha[i])