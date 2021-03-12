# recebe a altura e largura de um retângulo e o imprime com # no contorno e espaços no meio

i = w = int(input("digite a largura: "))
j = h = int(input("digite a altura: "))

while (j > 0):
    i = w
    while (i > 0):
        if (j != 1) and (j != h) and (i != 1) and (i != w): print(" ", end = "")
        else: print("#", end = "")
        i -= 1
    print()
    j -= 1