def produto_lincol(lin, a_mat, col, b_mat):
    '''(int, matriz, int, matriz) -> float

    Recebe duas matriz a_mat e b_mat e dois inteiros lin e col
    e calcula a soma do produto entre a linha lin de a_mat com
    a coluna col de b_mat

    Pre-condicao: a funcao supoe que o numero
       de colunas de a_mat e igual ao numero de linhas
       de b_mat
    '''
    soma = 0

    for lincol in range(len(a_mat[lin])):
            produto = a_mat[lin][lincol] * b_mat[lincol][col]
            soma += produto
    
    return soma


# teste
A = [ [1, 2, 1],
      [2, 2, 2],
      [1, 3, 2]]
B = [ [1, 1],
      [2, 0],
      [0, 1] ]
print(produto_lincol(1, A, 0, B))
