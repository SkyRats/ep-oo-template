import sys
import pytest

sys.path.append('../scripts')
from bateria import Bateria

CAPACIDADE = 1000
TEMPO_CARGA = 10
BATERIA = None

@pytest.fixture(autouse=True)
def reseta_bateria():
    global BATERIA
    BATERIA = Bateria(CAPACIDADE, TEMPO_CARGA)

def test_construtor():
    assert BATERIA._capacidade == CAPACIDADE
    assert BATERIA._tempoDeCarregamento == TEMPO_CARGA
    assert BATERIA._carga == 0
    assert BATERIA.calculaTempoDeVoo() == 0

def test_carregar():
    status_carregamento = BATERIA.carregar(0)
    assert not status_carregamento
    assert BATERIA._carga == 0

    status_carregamento = BATERIA.carregar(TEMPO_CARGA/2)
    assert status_carregamento
    assert BATERIA._carga == CAPACIDADE/2

    status_carregamento = BATERIA.carregar(TEMPO_CARGA/2)
    assert status_carregamento
    assert BATERIA._carga == CAPACIDADE

    status_carregamento = BATERIA.carregar(TEMPO_CARGA/2)
    assert not status_carregamento
    assert BATERIA._carga == CAPACIDADE

def test_usar():
    status_uso = BATERIA.usar(0)
    assert status_uso

    BATERIA.carregar(TEMPO_CARGA)
    status_uso = BATERIA.usar(0)
    assert status_uso
    assert BATERIA._carga == CAPACIDADE

    status_uso = BATERIA.usar(TEMPO_CARGA/2)
    assert status_uso
    assert BATERIA._carga == CAPACIDADE/2

    status_uso = BATERIA.usar(TEMPO_CARGA/2)
    assert status_uso
    assert BATERIA._carga == 0

    status_uso = BATERIA.usar(TEMPO_CARGA/2)
    assert status_uso
    assert BATERIA._carga == 0
