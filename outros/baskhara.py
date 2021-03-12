import math

a = float(input("a ="))
b = float(input ("b ="))
c = float(input ("c ="))

delta = (b ** 2) - (4 * a * c)

if (a == 0):
    x1 = - c / b
    print("Esta é uma equação de primeiro grau de raiz", x1)
else:
    if (delta < 0): print("A equação não tem raízes reais")
    else:
        x1 = (- b + math.sqrt(delta))/(2 * a)
        x2 = (- b - math.sqrt(delta))/(2 * a)

        if (delta == 0): print("A única raiz é", x1)
        else: print("As raízes são %.2f e %.2f" %(x1, x2))
