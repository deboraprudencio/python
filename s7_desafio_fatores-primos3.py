# recebe um número e retorna sua decomposição em fatores primos

n = int(input())
resultado = ""

if (n == 0): print("0^1")
if (n == 1): print("1^1")
if (n < 0):
    resultado += "- "
    n = - n

fator = 2

while (n > 1):
    
    potencia = 0

    while (n % fator == 0):
        potencia += 1
        n /= fator
    
    if (potencia != 0):
        resultado += str(fator) + "^" + str(potencia)
        if (n != 1): resultado += " * "

    fator += 1

print(resultado)