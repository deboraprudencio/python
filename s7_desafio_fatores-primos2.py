# recebe um número e retorna sua decomposição em fatores primos

def maior_primo (n): # recebe um número inteiro e retorna o maior número primo menor ou igual a ele

    while (n > 0):
        primo = True
        sqrt = n ** (1/2)
        i = 2

        while (i <= sqrt) and primo:
            if (n % i == 0):
                primo = False
            i += 1
        if primo: return n
        n -= 1

def main():
    fator = n = int(input())
    resultado = ""

    if (n == 0): print("0^1")
    if (n == 1): print("1^1")
    if (n < 0):
        resultado += "- "
        n = - n

    while (n > 1):
        
        fator = maior_primo(fator)
        potencia = 0

        while (n % fator == 0):
            potencia += 1
            n /= fator
        
        if (potencia != 0):
            resultado = str(fator) + "^" + str(potencia) + resultado
            if (n != 1): resultado = " * " + resultado

        fator -= 1

    print(resultado)

main()