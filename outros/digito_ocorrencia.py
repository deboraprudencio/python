n = int(input("Número:"))
d = int(input("Dígito:"))
vezes = 0

while (len(str(n)) > 0) and n != 0: #essa condição tem um problema pra númeroa que começam com 0 se o dígito também for 0
    if (n % 10 == d):
        vezes += 1
    n = n // 10

print("O dígito ocorre", vezes, "vezes no número")
