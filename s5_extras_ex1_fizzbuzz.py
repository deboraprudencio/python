def fizzbuzz (n):
    resultado = ""
    if (n % 3 == 0): resultado += "Fizz"
    if (n % 5 == 0): resultado += "Buzz"
    if (resultado == ""): resultado = n

    return resultado

def test_1():
    assert fizzbuzz (1) == 1

def test_2():
    assert fizzbuzz (2) == 2

def test_3():
    assert fizzbuzz (3) == "Fizz"

def test_4():
    assert fizzbuzz (4) == 4

def test_5():
    assert fizzbuzz (5) == "Buzz"

def test_6():
    assert fizzbuzz (6) == "Fizz"

def test_7():
    assert fizzbuzz (7) == 7

def test_8():
    assert fizzbuzz (8) == 8

def test_9():
    assert fizzbuzz (9) == "Fizz"

def test_10():
    assert fizzbuzz (10) == "Buzz"

def test_11():
    assert fizzbuzz (11) == 11

def test_12():
    assert fizzbuzz (12) == "Fizz"

def test_13():
    assert fizzbuzz (13) == 13

def test_14():
    assert fizzbuzz (14) == 14

def test_15():
    assert fizzbuzz (15) == "FizzBuzz"

def test_16():
    assert fizzbuzz (20) == "Buzz"

def test_17():
    assert fizzbuzz (21) == "Fizz"

def test_18():
    assert fizzbuzz (30) == "FizzBuzz"

def test_19():
    assert fizzbuzz (45) == "FizzBuzz"

def test_20():
    assert fizzbuzz (60) == "FizzBuzz"
