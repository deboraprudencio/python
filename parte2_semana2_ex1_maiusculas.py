def maiusculas(frase):
    ''' (str) -> str
    Recebe uma frase
    Devolve uma string com as letras maiúsculas que existem nesta frase, na ordem em que aparecem
    '''
    maiusculas = ''

    for letra in frase:
        if ord(letra) >= 65 and ord(letra) <= 90: maiusculas += letra
    
    return maiusculas

def teste_0():
    assert maiusculas('Programamos em python 2?') == 'P'

def teste_1():
    assert maiusculas('Programamos em Python 3.') == 'PP'

def teste_2():
    assert maiusculas('PrOgRaMaMoS em python!') == 'PORMMS'