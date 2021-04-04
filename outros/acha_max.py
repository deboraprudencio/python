def acha_max(A):
    '''(matriz) -> int, int, int

    Recebe uma matriz A e devolve 3 inteiros:
    k (um maior valor), e sua posicao lin, col.
    '''
    
    lin = col = 0
    k = A[lin][col]

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] > k:
                k = A[i][j]
                lin = i
                col = j

    
    return k, lin, col

# teste
A = [ [3, 7, 1], [1, 2, 8], [5, 3, 4]]
print(acha_max(A))
