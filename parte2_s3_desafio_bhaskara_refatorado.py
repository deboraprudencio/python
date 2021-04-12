# Recebe os parâmetros a, b e c de uma equação de segundo grau e retorna suas raízes

def main():
    a = float(input("a ="))
    b = float(input ("b ="))
    c = float(input ("c ="))

    (n_raizes, *raiz) = calcula_raizes(a, b, c)

    if n_raizes == 0: print("Esta equação não possui raízes reais")
    if n_raizes == 1: print("A raiz desta equação é", raiz)
    else:
        if (raiz[0] < raiz[1]): print("As raízes da equação são %.1f e %.1f" %(raiz[0], raiz[1]))
        else: print("As raízes da equação são %.1f e %.1f" %(raiz[1], raiz[0]))

def calcula_raizes(a, b, c):
    import math
    assert a != 0, "Esta não é uma equação de segundo grau"

    delta = (b ** 2) - (4 * a * c)
    if (delta < 0): return 0
    else:
        raiz1 = (- b + math.sqrt(delta))/(2 * a)
        raiz2 = (- b - math.sqrt(delta))/(2 * a)

        if (delta == 0): return 1, raiz1
        else: return 2, raiz1, raiz2
