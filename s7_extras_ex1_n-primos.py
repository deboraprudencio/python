# define e testa a função n_primos, que recebe um número maior ou igual a 2
# retorna quantos primos existem entre o número e 2, inclusive

def n_primos(n):
    primos = 0

    while (n > 1):
        i = 2
        primo = True
        sqrt = n ** (1/2)

        while (i <= sqrt) and primo:
            if (n % i == 0): primo = False
            i += 1

        if primo: primos += 1
        n -= 1

    return primos

def teste_1():
    assert n_primos(2) == 1

def teste_2():
    assert n_primos(4) == 2

def teste_3():
    assert n_primos(121) == 30