def incomodam(n):
    '''(int) --> str
        Devolve uma string contendo "incomodam " n vezes, usando recursão.
        Se n não for um inteiro estritamente positivo, a função deve devolver uma string vazia.
        '''
    if n < 1: return ""
    return "incomodam " + incomodam(n-1)

def elefantes(n):
    '''(int) --> str
        Devolve uma string contendo a letra da música "Um elefante incomoda muita gente" de 1 até n elefantes, usando recursão.
        Se n não for maior que 1, a função deve devolver uma string vazia.
        '''
        
    if n <= 1: return ""
    if n == 2: return "Um elefante incomoda muita gente\n" + str(n) + " elefantes " + incomodam(n) + "muito mais"
    
    trecho = str(n - 1) + " elefantes incomodam muita gente\n" + str(n) + " elefantes " + incomodam(n) + "muito mais"
    
    return elefantes(n - 1) + "\n" + trecho

import sys
if "pytest" in sys.modules:
    import pytest
    
    @pytest.mark.parametrize("n, musica",
        [(0, ""),
        (1, ""),
        (2, "Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais"), 
        (3, "Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais\n2 elefantes incomodam muita gente\n3 elefantes incomodam incomodam incomodam muito mais"),
        (4, "Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais\n2 elefantes incomodam muita gente\n3 elefantes incomodam incomodam incomodam muito mais\n3 elefantes incomodam muita gente\n4 elefantes incomodam incomodam incomodam incomodam muito mais")
        ])
    
    def teste(n, musica):
        assert elefantes(n) == musica

if __name__ == "__main__": print(elefantes(10))