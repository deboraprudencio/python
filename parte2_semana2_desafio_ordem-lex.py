def ordem_lex(lista):
    ''' (list) -> str
    Recebe uma lista de strings
    Devolve o primeiro na ordem lexicográfica
    Ignora maiúsculas e minúsculas
    '''

    primeiro = lista[0]

    for str in lista:
        if str.lower() < primeiro: primeiro = str
    
    return primeiro

def test_0():
    lista = ["ana     ", "josé", "Arquibaldo", "Julia"]
    assert ordem_lex(lista) == "ana     "

def test_1():
    lista = ["ana     ", "josé", "Arquibaldo       ", "    Julia"]
    assert ordem_lex(lista) == "    Julia"

def test_2():
    lista = ["zézão", "bia", "Bia     "]
    assert ordem_lex(lista) == "bia"

def test_3():
    lista = ["a", "ABC", "0123"]
    assert ordem_lex(lista) == "0123"
