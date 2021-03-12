# recebe a altura e a largura d eum retângulo e o imprime com #

i = w = int(input("digite a largura: "))
h = int(input("digite a altura: "))

while (h > 0):
    i = w
    while (i > 0):
        print("#", end = "")
        i -= 1
    print()
    h -= 1