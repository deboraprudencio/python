def divide (d, m, n):
    ''' (int, int, int) -> bool, int, int
    Recebe três inteiros positivos m, n, d
    Retorna False, m, n caso d não for divisor de m ou n.
    Caso contrário, retorna True, m’ e n’,
    Onde m’=m/d caso m for múltiplo de d e m’ = m caso contrário
    E n’=n/d caso n for múltiplo de d e n’ = n caso contrário.
    '''
    divide = False

    if (m % d == 0):
        m = m / d
        divide = True
    if (n % d == 0):
        n = n / d
        divide = True
    
    return (divide, m , n)

def primo(n):
    i = 2
    primo = True
    sqrt = n ** (1/2)

    while (i <= sqrt) and primo:
        if (n % i == 0): primo = False
        i += 1
    
    return primo

m = int(input())
n = int(input())
d = 2
mmc = 1

while m > 1 or n > 1:
    divisivel, m , n = divide(d, m, n)
    if divisivel: mmc *= d
    else:
        d += 1
        while not primo(d): d += 1

print(mmc)

