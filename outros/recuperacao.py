n = int(input("quantos alunos?"))
rec = 0

while (n > 0):
    nota = float(input("qual a nota?"))
    if (nota > 3) and (nota < 5): rec += 1
    n -= 1

print(rec, "alunos estão de recuperação")
