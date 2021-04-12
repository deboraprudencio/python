def marque_atacadas(tab):
    '''(tab) -> None
       Recebe um tabuleiro de xadrez (tab) e posições de rainhas (R)
       Altera tab marcando as posicoes atacadas por R com X
    '''
    for linha in tab:
        if linha.count('r') != 0:
            j_rainha = linha.index('r')
            i_rainha = tab.index(linha)
            break

    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if ((i_rainha == i) or (j_rainha == j) or (abs(i_rainha - i) == abs(j_rainha - j))) and tab[i][j] != 'R':
                tab[i][j] = 'X' 

tabuleiro = [ list('        '),
              list('        '),
              list('        '),
              list('        '),
              list('        '),
              list('        '),
              list('        '),
              list('        ') ]

n = int(input())

while n > 0:
    rainha = input().split(", ")
    tabuleiro[int(rainha[0])][int(rainha[1])] = 'r'
    marque_atacadas(tabuleiro)
    tabuleiro[int(rainha[0])][int(rainha[1])] = 'R'
    n -= 1

print("+---+---+---+---+---+---+---+---+")
for i in range(len(tabuleiro)):
    print("|", end = "")
    for j in range(len(tabuleiro)):
        print(" ", end = "")
        print(tabuleiro[i][j], end = " ")
        print("|", end = "")
    print()
    print("+---+---+---+---+---+---+---+---+")