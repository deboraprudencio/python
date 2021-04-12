class Ponto3D:

    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        s = "(%d, %d, %d)" %(self.x, self.y, self.z)
        return s
    
    def dist_origem(self):
        dist = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        return dist
    
    def dist_ponto(self, other):
        dist = ((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2) ** 0.5
        return dist
    
    def ponto_medio(self, other):
        x = (self.x + other.x) / 2
        y = (self.y + other.y) / 2
        z = (self.z + other.z) / 2
        return Ponto3D(x, y, z)

def teste():
    p1 = Ponto3D(4, -8, -9)
    p2 = Ponto3D(2, -3, -5)

    print(p1.dist_origem())
    print(p1.dist_ponto(p2))
    print(p1.ponto_medio(p2))

teste()