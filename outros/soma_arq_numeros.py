#-----------------------------------------------
def main():
    '''
    lê um arquivo com ao menos um numero real por linha
    calcula a soma de cada linha e a soma total
    '''

    linhas = []

    with open("numeros.txt", "w", encoding="utf-8") as arq:
        arq.write("5 4 3 2 1\n")
        arq.write("4 4 4\n")
        arq.write("2.7\n")
        arq.write("3.14 2.1\n")
    
    with open("numeros.txt", "r", encoding="utf-8") as arq:
        for linha in arq:
            linhas.append(linha.split(" "))
    
    total = 0

    for i in range(len(linhas)):
        soma = 0
        for j in range(len(linhas[i])):
            soma += float(linhas[i][j])
        print("Soma linha", i, "=", soma)
        total += soma
    
    print("Total =", total)

#-----------------------------------------------
main()