# para cada número digitado pelo usuário, devolve seu fatorial

n = int(input("Digite um número positivo: "))
while n >= 0:
    fatorial = 1

    while (n > 1):
        fatorial *= n 
        n -= 1
    
    print(fatorial)
    n = int(input("Digite um número positivo: "))