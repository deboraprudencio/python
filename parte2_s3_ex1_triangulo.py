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