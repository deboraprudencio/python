def fibonacci(n):
    ''' (int) --> int
        Recebe como parâmetro um número inteiro
        Devolve um número inteiro correspondente ao n-ésimo elemento da sequência de Fibonacci.
        '''
    if n <= 1: return n
    return fibonacci(n - 2) + fibonacci(n - 1)

import sys
if "pytest" in sys.modules:
    import pytest
    @pytest.mark.parametrize("n, resultado", 
        [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55)])
    def teste(n, resultado):
        assert fibonacci(n) == resultado

if __name__ == "__main__": print(fibonacci(10))