def main():
    '''
    Programa que le uma matriz de inteiros
    com m linha e n colunas e imprime o numero de linhas
    e de coluna nulas da matriz.
    '''
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

    def fileiras_nulas(matriz):
        n_linhas_nulas = 0
        n_colunas_nulas = 0

        for linha in range(len(matriz)):
            nulo = True
            for coluna in range(len(matriz[0])):
                if (matriz[linha][coluna] == 0) and nulo: nulo = True
                else: nulo = False
            if nulo: n_linhas_nulas += 1

        for coluna in range(len(matriz[0])):
            nulo = True
            for linha in range(len(matriz)):
                if (matriz[linha][coluna] == 0) and nulo: nulo = True
                else: nulo = False
            if nulo: n_colunas_nulas += 1

        print("Linhas nulas =", n_linhas_nulas)
        print("Colunas nulas =", n_colunas_nulas)

    fileiras_nulas(leia_matriz())

#-----------------------------------------------
main()