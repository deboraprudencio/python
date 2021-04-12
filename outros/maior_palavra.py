# #-----------------------------------------------
def main():
    '''
    lê uma linha com palavras separadas por vírgula e
    determina o comprimento da maior palavra.
    '''

    def separa(texto, sep):
        '''
        (str, str) -> list
        recebe um texto e separador, e devolve o texto separado
        '''
        txt_sep = []
        inicio = 0

        for i in range(len(texto)):
            if texto[i] == sep:
                txt_sep.append(texto[inicio:i])
                inicio = i + 1
        txt_sep.append(texto[inicio:])
        
        return txt_sep

    palavras = separa(input(), ",")
    maior_palavra = palavras[0]

    for palavra in palavras:
        if len(palavra) > len(maior_palavra): maior_palavra = palavra

    print(len(maior_palavra))

#-----------------------------------------------
main()
