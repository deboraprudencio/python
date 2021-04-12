def primeiro_lex(lista):
    ''' (list) -> str
    Recebe uma lista de strings
    Devolve o primeiro na ordem lexicográfica
    Ignora maiúsculas e minúsculas
    '''

    primeiro = lista[0]

    for str in lista:
        if str < primeiro: primeiro = str
    
    return primeiro

def test_0():
    lista = ["ana     ", "josé", "Arquibaldo", "Julia"]
    assert primeiro_lex(lista) == "Arquibaldo"

def test_1():
    lista = ["ana     ", "josé", "Arquibaldo       ", "    Julia"]
    assert primeiro_lex(lista) == "    Julia"

def test_2():
    lista = ["zézão", "bia", "Bia     "]
    assert primeiro_lex(lista) == "Bia     "

def test_3():
    lista = ["a", "ABC", "0123"]
    assert primeiro_lex(lista) == "0123"

def test_4():
    assert primeiro_lex(['oĺá', 'A', 'a', 'casa']) == 'A'

def test_5():
    assert primeiro_lex(['AAAAAA', 'b']) == 'AAAAAA'
