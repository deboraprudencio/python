# recebe um número m > 0
# n assume valores de 1 a m
# retorna os ímpares consecutivos cuja soma é igual a n**3

m = int(input())
n = 1

while (n <= m):
    resposta = ""
    
    print("%d**3 = " %n, end = "")

    mid = int((n ** 3) / n)
    i = - (n - 1)

    while (i < n):
        resposta += str(mid + i)
        if ((i + 2) < n): resposta += " + "
        i += 2

    print(resposta)
    n += 1