# recebe um número inteiro e retorna a soma de seus dígitos

n = int(input())
soma = 0

while (n != 0):
    soma += n % 10
    n = n // 10

print(soma)
