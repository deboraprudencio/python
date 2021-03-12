def computador_escolhe_jogada(n, m):
    '''Realiza a jogada do computador

    Recebe o número de peças no tabuleiro (n)
    Recebe o número máximo de peças que podem ser retiradas por jogada (m)
    Devolve o número de peças que o computador retira do tabuleiro (p)
    '''

    p = m

    while (p > 0):
        if ((n - p) % (m + 1) == 0): return p
        p -= 1
    return m

def usuario_escolhe_jogada(n, m):
    '''Realiza a jogada do usuário

    Recebe o número de peças no tabuleiro (n)
    Recebe o número máximo de peças que podem ser retiradas por jogada (m)
    Pede que o jogador informe sua jogada (p) até receber um valor válido
    Devolve as peças removidas pelo usuário
    '''

    while True:
        p = int(input("Quantas peças você quer tirar da mesa? "))

        if (1 <= p) and (p <= m): return p
        else: print("Esta não é uma quantidade válida. Por favor digite um número entre 1 e", m)

def partida():
    '''Inicializa o jogo, controla as rodadas e finaliza o jogo

    Pede que o jogador informe o número inicial de peças no tabuleiro (n)
    Pede que o jogador informe o máximo de peças que podem ser retiradas por jogada (m)
    Inicia o jogo, alternando as jogadas do usuário e do computador
    Escolhe quem realiza a jogada inicial, favorecendo o computador
    Imprime quantas peças foram removidas na última rodada (p)
    Imprime quantas peças restam na mesa (n)
    Quando a última peça é removida, imprime o vencedor
    '''

    n = int(input("Digite o número inicial de peças na mesa: "))
    m = int(input("Digite o máximo de peças que poderão ser removidas por vez: "))
    print("-----------------")
    comp_turn = True

    if (n % (m + 1) == 0):
        print("Você começa!")
        comp_turn = False
    else:
        print("Computador começa!")
        comp_turn = True

    while (n > 0):
        if comp_turn:
            print ("----------------- \nVez do computador! \n")
            p = computador_escolhe_jogada(n, m)
            comp_turn = False
        else:
            print ("----------------- \nSua vez! \n")
            p = usuario_escolhe_jogada(n, m)
            comp_turn = True

        n -= p
        print(p, "peças foram removidas")
        print(n, "peças restam na mesa")

    if comp_turn:
        print("----------------- \nVocê ganhou!")
        return False
    else:
        print("----------------- \nO computador ganhou!")
        return True

def campeonato():
    comp_pt = 0
    user_pt = 0
    i = 1

    print("\nBem vindo ao jogo do Nim! \nJogue contra o computador e tente ser o último a tirar uma peça da mesa \n-----------------")

    while (comp_pt < 3) and (user_pt < 3):
        print("\n\nRodada", i)
        if partida(): comp_pt += 1
        else: user_pt += 1
        i += 1

    print("\n\nPlacar: Você %d X %d Computador" %(user_pt, comp_pt))

    play_again = input("Digite 'nim' para jogar novamente")
    if (play_again == "nim"): campeonato()

campeonato ()
