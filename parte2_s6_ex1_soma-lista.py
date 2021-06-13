def soma_lista(lista):
    ''' (list) --> int
        Recebe como parâmetro uma lista de números inteiros
        Devolve a soma dos elementos desta lista.
        '''
    soma = lista[0]
    if len(lista) == 1: return lista[0]
    else: return soma + soma_lista(lista[1:])

import sys
if "pytest" in sys.modules:
    import pytest
    @pytest.mark.parametrize("lista, resultado", [([1, 2, 3], 6), ([0, 0, 0], 0), ([-1, 2, -3], -2)])
    def teste(lista, resultado):
        assert soma_lista(lista) == resultado