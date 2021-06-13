def encontra_impares(lista):
    ''' (list) --> list
        Recebe como parâmetro uma lista de números inteiros
        Devolve uma outra lista apenas com os números ímpares da lista dada
        '''
    impares = []

    if len(lista) > 0:
        if lista[0] % 2 != 0: impares.append(lista[0])
        impares.extend(encontra_impares(lista[1:]))

    return impares

import sys
if "pytest" in sys.modules:
    import pytest
    
    @pytest.mark.parametrize("lista, resultado", [
        ([1, 2, 3], [1, 3]), ([2, 2, 2], []), ([1, 1, 1], [1, 1, 1]),
        ([1, 2, 1], [1, 1]), ([2, 1, 2], [1]), ([], [])
        ])
    
    def teste(lista, resultado):
        assert encontra_impares(lista) == resultado

if __name__ == "__main__": print(encontra_impares([1, 2, 3, 4]))