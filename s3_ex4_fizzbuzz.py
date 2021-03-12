#recebe um número e retorna "fizzbuzz" se ele for múltiplo de 3 e de 5, senão retorna o número

n = int(input())

if (n % 3 == 0) and (n % 5 == 0): print("FizzBuzz")
else: print(n)
