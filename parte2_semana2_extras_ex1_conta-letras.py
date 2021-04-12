def conta_letras(frase, contar="vogais"):
    ''' (str, str) -> int
    Recebe como primeiro parâmetro uma string contendo uma frase e como segundo parâmetro (opcional) outra string.
    Quando o segundo parâmetro é "vogais", a função devolve o numero de vogais presentes na frase.
    Quando o segundo parâmetro é "consoantes", a função devolve o número de consoantes presentes na frase.
    '''

    qtd_vogais = frase.count("a") + frase.count("e") + frase.count("i") + frase.count("o") + frase.count("u")
    if contar == "vogais": return qtd_vogais
    else: return len(frase) - qtd_vogais - frase.count(" ")

def test_0():
    assert conta_letras('programamos em python') == 6

def test_1():
    assert conta_letras('programamos em python', 'vogais') == 6

def test_2():
    conta_letras('programamos em python', 'consoantes') == 13