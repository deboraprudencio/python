def computador_escolhe_jogada(n, m):
    p = m
    while (p > 0):
        if ((n - p) % (m + 1) == 0): return p
        p -= 1
    return m

def usuario_escolhe_jogada(n, m):
    while True:
        p = int(input("\nQuantas peças você vai tirar? "))

        if (1 <= p) and (p <= m): return p
        else: print("\nOops! Jogada inválida! Tente de novo.")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    comp_turn = True

    if (n % (m + 1) == 0):
        print("Você começa!")
        comp_turn = False
    else:
        print("Computador começa!")
        comp_turn = True

    while (n > 0):
        if comp_turn:
            p = computador_escolhe_jogada(n, m)
            comp_turn = False
            print("\nO computador tirou %d peça(s)." %(p))
        else:
            p = usuario_escolhe_jogada(n, m)
            comp_turn = True
            print("Você tirou %d peça(s)." %(p))

        n -= p
        print("Agora restam %d peça(s) no tabuleiro." %n)

    print("\nFim do jogo!")
    if comp_turn:
        print("Você ganhou!")
        return False
    else:
        print("O computador ganhou!")
        return True

def campeonato():
    i = 1
    comp_pt = 0
    user_pt = 0

    while (i <= 3):
        print("\n**** Rodada %d ****\n" %(i))
        if partida(): comp_pt += 1
        else: user_pt += 1
        i += 1

    print("\n**** Final do campeonato! ****\n")
    print("Placar: Você %d X %d Computador" %(user_pt, comp_pt))

tipo = 0
while (tipo != 1) and (tipo != 2):
    tipo = input("\nBem-vindo ao jogo do NIM! Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato ")
    if (tipo == "1"):
        print("\nVocê escolheu uma partida!")
        partida()
    elif (tipo == "2"):
        print("\nVocê escolheu um campeonato!")
        campeonato()
