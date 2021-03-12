# define e testa a função soma_hipotenusas() que recebe um número inteiro
# devolve todos os inteiros entre 1 e n que são hipotenusas de algum triângulo retângulo com catetos inteiros

def hipotenusa(n):
    max_cateto = ((n ** 2) - 1) ** (1/2)
    i = 1
    while (i < max_cateto):
        j = 1
        while (j < max_cateto):
            if (n == (((i ** 2) + (j ** 2)) ** (1/2))): return True
            j += 1
        i += 1
    
    return False


def soma_hipotenusas(n):
    soma = 0
    while (n > 0):
        if hipotenusa(n): soma += n
        n -= 1
    
    return soma

def test_1():
    assert soma_hipotenusas(25) == 105

def test_2():
    assert soma_hipotenusas(1) == 0
