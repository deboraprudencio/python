n = int(input("Quantidade de números:"))
par = 0
impar = 0

print("Digite os números: ")

while (n > 0):
    num = int(input())

    if (num % 2 == 0): par += 1
    else: impar += 1

    n -= 1

print(par, "pares e", impar, "ímpares")
