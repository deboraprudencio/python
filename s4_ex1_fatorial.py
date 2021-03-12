# recebe um número inteiro e retorna o fatorial desse número

n = int(input())
fat = 1

while (n > 0):
    fat *= n 
    n -= 1

print(fat)
