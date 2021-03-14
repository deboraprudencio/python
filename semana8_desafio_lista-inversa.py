# recebe uma lista de números do usuário
# retorna a lista em ordem inversa

n = []
i = 1

while (i != 0):
    i = int(input())
    n.append(i)

i = len(n) - 2

while (i >= 0):
    print(n[i])
    i -= 1