BOMBA = -1
LIVRE = 0

def main(A):
    '''
    Recebe uma matriz A com 0's e -1's e calcula a quantidade de
    bombas ao redor de cada posição livre.
    '''

    def conta_bomba(A, lin, col):
        '''
        Recebe uma matriz inteira A e uma posicao (lin, col), e
        retorna o numero de bombas ao redor de (lin, col)
        '''
        qtd_bombas = 0

        for i in range(lin - 1, lin + 2):
            for j in range(col - 1, col + 2):
                if i >= 0 and j >= 0 and i < len(A) and j < len(A[i]) and A[i][j] == BOMBA: qtd_bombas += 1
        
        return qtd_bombas

    for lin in range(len(A)):
        for col in range(len(A)):
            if A[lin][col] == LIVRE: A[lin][col] = conta_bomba(A, lin, col)
    
    return A

#-----------------------------------------------
print(main([[0, 0, 0, 0, -1], [-1, -1, 0, 0, 0], [0, 0, 0, -1, 0], [-1, -1, -1, 0, 0], [0, -1, 0, -1, 0]]))
