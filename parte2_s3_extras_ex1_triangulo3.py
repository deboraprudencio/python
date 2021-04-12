''' Define a classe Triangulo
    Possui atributos a, b e c correspondentes aos lados de um triângulo
    Possui o método perimetro, que não recebe parâmetros e devolve o perímetro do triângulo.
'''
class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        ab = self.a == self.b
        ac = self.a == self.c
        bc = self.b == self.c

        if ab and bc: return 'equilátero'
        elif ab or ac or bc: return 'isósceles'
        else: return 'escaleno'
    
    def retangulo(self):
        hip_a = self.a ** 2 == self.b ** 2 + self.c ** 2
        hip_b = self.b ** 2 == self.a ** 2 + self.c ** 2
        hip_c = self.c ** 2 == self.a ** 2 + self.b ** 2

        if hip_a or hip_b or hip_c: return True
        else: return False