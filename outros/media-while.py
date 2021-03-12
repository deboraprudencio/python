# recebe um número n de alunos, pede n notas e calcula a média aritmética dessas notas

n = int(input("Quantos alunos?"))
soma = 0

while (n > 0):
    nota = float(input("Qual a nota?"))
    soma += nota
    n -= 1

media = soma / nota
print("A média é", media)
