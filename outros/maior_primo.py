def maior_primo (n):

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

n = int(input())
print(maior_primo(n))