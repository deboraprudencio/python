# recebe os parâmetros a, b e c de uma equação de segundo grau e retorna suas raízes

import math

a = float(input("a ="))
b = float(input ("b ="))
c = float(input ("c ="))

delta = (b ** 2) - (4 * a * c)

if (a == 0):
    x1 = - c / b
    print("Esta é uma equação de primeiro grau de raiz", x1)
else:
    if (delta < 0): print("esta equação não possui raízes reais")
    else:
        x1 = (- b + math.sqrt(delta))/(2 * a)
        x2 = (- b - math.sqrt(delta))/(2 * a)

        if (delta == 0): print("a raiz desta equação é", x1)
        else:
            if (x1 < x2): print("as raízes da equação são %.1f e %.1f" %(x1, x2))
            else: print("as raízes da equação são %.1f e %.1f" %(x2, x1))
