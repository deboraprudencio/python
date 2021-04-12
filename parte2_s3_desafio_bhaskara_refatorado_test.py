import pytest
import parte2_s3_desafio_bhaskara_refatorado

@pytest.fixture
def resultado():
    return parte2_s3_desafio_bhaskara_refatorado

@pytest.mark.parametrize("a, b, c, resultado_esperado", [
    (1, 0, 0, (1, 0)),
    (1, -5, 6, (2, 3, 2)),
    (10, 10, 10, 0),
    (10, 20, 10, (1, -1)),
])

def test(resultado, a, b, c, resultado_esperado):
    assert resultado.calcula_raizes(a, b, c) == resultado_esperado