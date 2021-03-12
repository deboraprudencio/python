#recebe as coordenadas x e y de 2 pontos e retorna a distância entre eles

import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if (dist >= 10): print("longe")
else: print("perto")
