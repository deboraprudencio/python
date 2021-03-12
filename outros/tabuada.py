# imprime a tabuada até 10

linha = 1
coluna = 1

while (coluna <= 10):
    while (linha <= 10):
        print(coluna * linha, end = "\t")
        linha += 1
    coluna +=1
    linha = 1
    print()