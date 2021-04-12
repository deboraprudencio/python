class Racional:
    def __init__(self, numerador = 0, denominador = 1):
        self.num = numerador
        self.den = denominador
        self.simplifica()
    
    def __str__(self):
        if self.den == 1: s = str(self.num)
        elif self.num % self.den == 0: s = str(self.num // self.den)
        else: s = str(self.num) + "/" + str(self.den)

        return s
    
    def simplifica(self):
        n1, n2 = self.num, self.den

        while (n1 != 0) and (n2 != 0):
            if (n1 > n2): n1 -= n2
            else: n2 -= n1

        if (n1 == 0): mdc = n2
        else: mdc = n1

        self.num //= mdc
        self.den //= mdc

        return self
    
    def __add__(self, n):
        num = (self.num * n.den) + (n.num * self.den)
        den = self.den * n.den

        return Racional(num, den).simplifica()
    
    def __sub__(self, n):
        num = (self.num * n.den) - (n.num * self.den)
        den = self.den * n.den

        return Racional(num, den).simplifica()
    
    def __mul__(self, n):
        num = self.num * n.num
        den = self.den * n.den

        return Racional(num, den).simplifica()
    
    def __truediv__(self, n):
        num = self.num * n.den
        den = self.den * n.num

        return Racional(num, den).simplifica()

def teste():
    r1 = Racional(25, 20)
    r2 = Racional(5, 10)
    r3 = Racional()
    r4 = Racional(2)
    r5 = Racional(denominador = 5)

    print("r1 =", r1)
    print("r2 =", r2)
    print("r3 =", r3)
    print("r4 =", r4)
    print("r5 =", r5)

    print("r1 + r2 =", r1.__add__(r2))
    print("r1 * r2 =", r1.__mul__(r2))
    print("r1 - r2 =", r1.__sub__(r2))
    print("r1 / r2 =", r1.__truediv__(r2))
    
    print("é o mesmo que", r1 + r2, "e", r1 * r2, "e", r1 - r2, "e", r1 / r2)

teste()