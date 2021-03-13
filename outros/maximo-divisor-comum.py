# recebe n números e retorna o seu máximo divisor comum

n = int(input())
n_prev = 1
max_div = 1

while (n > 0):
    i = n_novo = int(input())
    if (max_div != 1): i = max_div
    elif (n_prev < n_novo): i = n_prev
    
    while (i > 1):
        if (n_novo % i == 0) and (n_prev % i == 0):
            max_div = i
            i = 1
        i -= 1
        
    n_prev = n_novo
    n -= 1

print("Máximo divisor comum:", max_div)