class Complexo:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a == 0: str(self.b) + "i"
        elif self.b == 0: s = str(self.a)
        elif self.b > 0: s = str(self.a) + "+" + str(self.b) + "i"
        else: s = str(self.a) + str(self.b) + "i"
        return s

    def soma(self, num):
        self.a = self.a + num.a
        self.b = self.b + num.b
        print(self)

    def multiplica(self, num):
        c = self.a * num.a - self.b * num.b
        d = self.a * num.b + self.b * num.a
        self.a, self.b = c, d
        print(self)
    
def teste():
    c1 = Complexo(1, 2)
    c2 = Complexo(1, 3)

    c1.soma(c2)
    c1.multiplica(c2)

teste()