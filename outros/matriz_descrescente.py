#-----------------------------------------------
def main():
    '''
    Recebe uma matriz quadrada de inteiros de dimensao nl x nc,
    e imprime os seus valores em ordem decrescente.
    '''
    # escreva o seu programa abaixo e remova o print()

    def acha_max(matriz):
        '''(matriz) -> int, int, int

        Recebe uma matriz A e devolve 3 inteiros:
        k (um maior valor), e sua posicao lin, col.
        '''
        
        lin = col = 0
        max = matriz[lin][col]

        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] and matriz[i][j] > max:
                    max = matriz[i][j]
                    lin = i
                    col = j

        
        return max, lin, col

    def matriz_descrescente(matriz):
        print("Elem \t Linha \t Coluna")
        
        for i in range(len(matriz) ** 2):
            max, lin, col = acha_max(matriz)
            matriz[lin][col] = False
            print(max, "\t", lin, "\t", col)

    matriz_descrescente([[3, 7, 1], [1, 2, 8], [5, 3, 4]])

#-----------------------------------------------
main()
