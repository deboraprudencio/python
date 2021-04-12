import racional

def main():
    # modifique o codigo para incluir o calculo de DE (direita para esquerda)
    # e verifique se o resultado é diferente de ED (esquerda para direita) usando
    # soma de reais e soma de racionais.

    n = 50
    soma_ed = 0
    soma_ed_rac = racional.Racional()
    soma_de = 0
    soma_de_rac = racional.Racional()

    for i in range(1, n+1):
        soma_ed += 1/i
        soma_de += 1/(n+1-i)
        soma_ed_rac += racional.Racional(1, i)
        soma_de_rac += racional.Racional(1, (n+1-i))

    print("Soma ED:          ", soma_ed)
    print("Soma ED racional: ", soma_ed_rac)
    print("                = ", soma_ed_rac.num/soma_ed_rac.den)
    print("Soma DE:          ", soma_de)
    print("Soma DE racional: ", soma_de_rac)
    print("                = ", soma_de_rac.num/soma_de_rac.den)

def mdc(a, b):
    ''' (int, int) -> int
        recebe dois inteiros diferentes de zero e retorna o maximo
        divisor comum entre a e b'''
    if b == 0: return a
    if a == 0: return b
    while a%b != 0:
        a, b = b, a%b
    return b

main()

# pou seja, com a soma de racionais elimina-se o problema!