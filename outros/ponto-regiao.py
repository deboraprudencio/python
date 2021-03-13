# recebe as coordenadas x e y de um ponto
# retorna se ela está dentro ou fora da região cinza
# região: https://panda.ime.usp.br/aulasPython/static/aulasPython/exercicios/ex81a.html

def dentro(x,y):
    if x < 0: x = - x
    
    if (y > 5 and y < 6) and (x > 2 and x < 3): return "dentro"
    elif ((y >= 8 or y <= 0 or x >= 5)
        or ((y >= 4 and y <= 7) and (x >= 1 and x <=4))
        or ((y >= 1 and y <= 2) and (x <= 3))): 
        return "fora"
    else: return "dentro"

x = float(input())
y = float(input())

print(dentro(x,y))
