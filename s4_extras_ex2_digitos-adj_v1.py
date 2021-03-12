# recebe um número e retorna se ele contém dígitos adjacentes iguais ou não
# usa o método exit() do módulo sys

import sys

n = int(input())

while (len(str(n)) >= 2):
    lastDig = n % 10
    prevDig = (n // 10) % 10

    n = n // 10

    if (lastDig == prevDig):
        print("o número contém dígitos adjacentes iguais")
        exit()

print ("o número não contém dígitos adjacentes iguais")
