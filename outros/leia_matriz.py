def leia_matriz():
    n_linhas = int(input("Digite o número de linhas:"))
    n_colunas = int(input("Digite o número de colunas:"))
    matriz = []

    for i in range(n_linhas):
        print("matriz =", matriz)
        linha = []

        for j in range(n_colunas):
            print("linha %d = %s" %(i, linha))
            linha.append(int(input("Digite o elemento (%d,%d):" %(i,j))))
            
        matriz.append(linha)
    
    return matriz