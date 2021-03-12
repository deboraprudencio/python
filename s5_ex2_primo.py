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

def test_1():
    assert maior_primo (100) == 97

def test_2():
    assert maior_primo (7) == 7

def test_3():
    assert maior_primo (7900) == 7883

def test_4():
    assert maior_primo (7910) == 7907
