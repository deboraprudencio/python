i = n = int(input("Quantos alunos?"))
rep = rec = apr = bom = 0

while (i > 0):
    nota = float(input("Qual a nota?"))

    if (nota < 3): rep += 1
    elif (3 <= nota < 5): rec += 1
    elif (5 <= nota): apr += 1
    if (8 < nota): bom += 1

    i -= 1

print("Total de alunos =", n)
print("Número de alunos reprovados =", rep)
print("Número de alunos de recuperação =", rec)
print("Número de alunos aprovados =", apr)
print("Número de alunos com desempenho muito bom =", bom)
