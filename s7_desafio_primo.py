#recebe um número e retorna se ele é primo ou não

n = int(input("Digite um número inteiro: "))

def primo(n):
    i = 2
    primo = True
    sqrt = n ** (1/2)

    while (i <= sqrt) and primo:
        if (n % i == 0): primo = False
        i += 1
    
    return primo

while (n > 0):
    if primo(n): print(n, "é primo!")
    else: print(n, "não é primo :(")
    
    n = int(input("Digite um número inteiro: "))