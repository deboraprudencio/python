# recebe dois números i e j e uma quantia n
# imprime os n primeiros números múltiplos de i, j ou ambos

n = int(input())
i = int(input())
j = int(input())
cont = 0

while (n > 0):
    if (cont % i == 0) or (cont % j == 0):
        print(cont, end = " ")
        n -= 1
    cont += 1