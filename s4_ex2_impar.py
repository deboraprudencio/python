# recebe um número n e imprime os n primeiros números ímpares

n = int(input())
i = 1

while (n > 0):
    if (i % 2 != 0):
        print(i)
        n -= 1
    i += 1
