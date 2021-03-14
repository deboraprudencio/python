# recebe n números e retorna se são uma progressão aritmética

n = int(input())

def isPA (n):
    n_old = i = dif = 0

    while (i < n):
        n_new = int(input())

        if (i <= 1): dif = n_new - n_old
        elif (n_new - n_old != dif): return "Não é uma progressão aritmética"
        
        n_old = n_new
        i += 1

    return "É uma progressão aritmética"

print(isPA(n))