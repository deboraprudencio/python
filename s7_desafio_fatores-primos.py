# recebe um número e retorna sua decomposição em fatores primos

def prox_primo(n): # recebe um número e retorna o menor número primo maior que ele

    while True:
        n += 1
        i = 2
        primo = True

        while (i <= n ** (1/2)):
            if (n % i == 0): primo = False
            i += 1
    
        if primo: return n

def main():
    n = int(input())
    resultado = ""

    if (n == 0): print("0^1")
    if (n == 1): print("1^1")
    if (n < 0):
        resultado += "- "
        n = - n

    fator = 1
    while (fator <= n):
        
        fator = prox_primo(fator)
        potencia = 0

        while (n % fator == 0):
            potencia += 1
            n /= fator
        
        if (potencia != 0):
            resultado += str(fator) + "^" + str(potencia)
            if (n != 1): resultado += " * "

    print(resultado)

main()