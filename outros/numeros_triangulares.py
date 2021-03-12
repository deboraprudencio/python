import sys

n = int(input())
i = int(n ** (1/3)) + 1
produto = 0

while (produto < n):

    produto = (i - 1) * i * (i + 1)
    i += 1

    if(produto == n):
        print("é triangular")
        exit()

print("não é triangular")
