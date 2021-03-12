n = int(input("Qual o número?"))
k = int(input("Qual a classe?"))

def fatorial(n):
    fat = 1
    while (n > 1):
        fat *= n
        n -= 1

    return fat

def coefBinomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n - k))

print(coefBinomial(n, k))
