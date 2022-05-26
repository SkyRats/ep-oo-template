import sys
sys.path.append('../scripts')

import pytest
from bateria import Bateria

from helper import get_attr

CAPACIDADE = 1000
TEMPO_CARGA = 10
BATERIA = None

@pytest.fixture(autouse=True)
def reseta_bateria():
    global BATERIA
    BATERIA = Bateria(CAPACIDADE, TEMPO_CARGA)

def test_construtor():
    assert get_attr(BATERIA, 'mah') == CAPACIDADE
    assert get_attr(BATERIA, 'tempoDeCarregamento') == TEMPO_CARGA
    assert get_attr(BATERIA, 'carga') == 0
    assert BATERIA.calcula_tempo_de_voo() == 0

def test_carregar():
    status_carregamento = BATERIA.carregar(0)
    assert not status_carregamento
    assert get_attr(BATERIA, 'carga') == 0

    status_carregamento = BATERIA.carregar(TEMPO_CARGA/2)
    assert status_carregamento
    assert get_attr(BATERIA, 'carga') == CAPACIDADE/2

    status_carregamento = BATERIA.carregar(TEMPO_CARGA/2)
    assert status_carregamento
    assert get_attr(BATERIA, 'carga') == CAPACIDADE

    status_carregamento = BATERIA.carregar(TEMPO_CARGA/2)
    assert not status_carregamento
    assert get_attr(BATERIA, 'carga') == CAPACIDADE

def test_usar():
    status_uso = BATERIA.usar(0)
    assert status_uso

    BATERIA.carregar(TEMPO_CARGA)
    status_uso = BATERIA.usar(0)
    assert status_uso
    assert get_attr(BATERIA, 'carga') == CAPACIDADE

    status_uso = BATERIA.usar(TEMPO_CARGA/2)
    assert status_uso
    assert get_attr(BATERIA, 'carga') == CAPACIDADE/2

    status_uso = BATERIA.usar(TEMPO_CARGA/2)
    assert status_uso
    assert get_attr(BATERIA, 'carga') == 0

    status_uso = BATERIA.usar(TEMPO_CARGA/2)
    assert status_uso
    assert get_attr(BATERIA, 'carga') == 0
