def multi_matriz(a_mat, b_mat):
    '''(matriz,matriz) -> matriz

    Recebe duas matriz a_mat e b_mat e cria e retorna
    a matriz produto  de a_mat por b_mat.

    Pre-condicao: a funcao supoe que o numero
       de coluna de a_mat e igual ao numero de linhas
       de b_mat
    '''
    matriz_produto = []

    for lin_a in range(len(a_mat)):
        linha_somas = []
        for col_b in range(len(b_mat[0])):
            soma = 0
            for col_lin in range(len(a_mat[lin_a])):
                produto_elementos = a_mat[lin_a][col_lin] * b_mat[col_lin][col_b]
                soma += produto_elementos
            linha_somas.append(soma)    
        matriz_produto.append(linha_somas)
    
    return matriz_produto


#----------------------------------------------
# teste
a = [ [1, 2, -1], [0, 3, 2] ]
b = [ [1, -1], [2, 0], [3, 2] ]
c = multi_matriz(a,b)
resultado = [ [2, -3], [12, 4] ]
if c == resultado:
    print("Passou no primeiro teste! :-)")
else:
    print("Nao passou no primeiro teste! :-(")

# colocar mais testes abaixo

a = [ [1, 2], [3, 4] ]
b = [ [-1, 3], [4, 2] ]
c = multi_matriz(a,b)
resultado = [ [7, 7], [13, 17] ]
if c == resultado:
    print("Passou no segundo teste! :-)")
else:
    print("Nao passou no segundo teste! :-(")

a = [ [1, 2], [3, 4] ]
b = [ [-1, 3], [4, 2] ]
c = multi_matriz(b,a)
resultado = [ [8, 10], [10, 16] ]
if c == resultado:
    print("Passou no terceiro teste! :-)")
else:
    print("Nao passou no terceiro teste! :-(")

a = [ [2, 3], [0, 1], [-1, 4] ]
b = [ [1, 2, 3], [-2, 0, 4] ]
c = multi_matriz(a,b)
resultado = [ [-4, 4, 18], [-2, 0, 4], [-9, -2, 13] ]
if c == resultado:
    print("Passou no quarto teste! :-)")
else:
    print("Nao passou no quarto teste! :-(")

a = [ [2, 3], [0, 1], [-1, 4] ]
b = [ [1, 2, 3], [-2, 0, 4] ]
c = multi_matriz(b,a)
resultado = [ [-1, 17], [-8, 10] ]
if c == resultado:
    print("Passou no quinto teste! :-)")
else:
    print("Nao passou no quinto teste! :-(")
