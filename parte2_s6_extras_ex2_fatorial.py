def fatorial(n):
    ''' (int) --> int
        Recebe como parâmetro um número inteiro
        Devolve um número inteiro correspondente ao fatorial deste número
        '''
    if n <= 1: return 1
    return n * fatorial(n - 1)

import sys
if "pytest" in sys.modules:
    import pytest
    @pytest.mark.parametrize("n, resultado", 
        [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24), (5, 120), (6, 720)])
    def teste(n, resultado):
        assert fatorial(n) == resultado

if __name__ == "__main__": print(fatorial(10))