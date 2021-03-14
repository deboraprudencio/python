# recebe dois números inteiros
# retorna o seu máximo divisor comum usando o algoritmo de euclides

n1 = int(input())
n2 = int(input())

while (n1 != 0) and (n2 != 0):
    if (n2 > n1): n2 = n2 - n1
    else: n1 = n1 - n2

if (n1 == 0): print(n2)
else: print(n1)