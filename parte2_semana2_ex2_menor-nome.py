def menor_nome(nomes):
    ''' (list) -> str
    Recebe uma lista de nomes (strings)
    Devolve o nome mais curto
    Ignora espaços antes ou depois e capitaliza a primeira letra
    '''

    menor_nome = nomes[0]

    for nome in nomes:
        nome = nome.strip()
        if len(nome) < len(menor_nome): menor_nome = nome
    
    return menor_nome.capitalize()

def test_0():
    assert menor_nome(["ana     ", "josé", "Arquibaldo", "Julia"]) == "Ana"

def test_1():
    assert menor_nome(["       ana     ", "josé", "Arquibaldo       ", "Julia"]) == "Ana"

def test_2():
    assert menor_nome(["zézão", "Pedro", "       ana     "]) == "Ana"

def test_3():
    assert menor_nome(['maria', 'josé', 'PAULO', 'Catarina']) == 'José'

def test_4():
    assert menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']) == 'José'
    
def test_5():
    assert menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']) == 'José'

def test_6():
    assert menor_nome(['zé', ' lu', 'fê']) == 'Zé'
    
def test_7():
    assert menor_nome([' zé', ' lu', '      fê']) == 'Zé'