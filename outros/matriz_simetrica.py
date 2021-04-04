def simetrica(matriz):
    '''(matriz) -> bool

    Recebe uma matriz e returna True se a matriz for simetrica,
    em caso contrario retorna False.

    Pre-condicao: a funcao supoe que a matriz e quadrada

    '''
    simetrica = True

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (matriz[i][j] != matriz[j][i]): simetrica = False
    
    return simetrica

#-----------------------------------------------------
# testes
a = [[11, -3, 4, 8], [-3, 12, 6, 11], [4, 6, 5, 13], [8, 11, 13, 5]]
if simetrica(a):
    print("Passou no primeiro teste! :-)")
else:
    print("Nao passou no primeiro teste! :-(")