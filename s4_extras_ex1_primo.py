n = int(input())
i = 2
primo = True
sqrt = n ** (1/2)

while (i <= sqrt) and primo:
    if (n % i == 0):
        primo = False
    i += 1

if primo: print("primo")
else: print("não primo")
