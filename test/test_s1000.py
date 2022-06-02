import sys
sys.path.append('../scripts')

import pytest
from helper import get_attr
from bateria import Bateria
from s1000 import S1000

CAPACIDADE = 1000
TEMPO_CARGA = 30
batS1000 = None

NOME = "Nome_teste"
POSICAO = 0
s1000 = None

ALTURA_S1000 = 2.0
POSICAO_SET_POSITION = 10

@pytest.fixture(autouse=True)
def reseta_drone():
    global s1000
    global batS1000
    batS1000 = Bateria(CAPACIDADE, TEMPO_CARGA)
    s1000 = S1000(NOME, batS1000, POSICAO)

def test_construtor():
    assert get_attr(s1000, 'nome') == NOME
    assert get_attr(s1000, 'altura') == 0.0
    assert get_attr(s1000, 'decolado') == False

def test_mapear():
    statusS1000 = False
    get_attr(s1000, 'bateria').carregar(TEMPO_CARGA)
    s1000.takeoff(ALTURA_S1000)
    statusS1000 = s1000.mapear()

    assert statusS1000 == True

def test_mapearSemBateria():
    statusS1000 = False
    s1000.takeoff(ALTURA_S1000)
    statusS1000 = s1000.mapear();

    assert statusS1000 == False

def test_mapearSemTakeoff():
    get_attr(s1000, 'bateria').carregar(TEMPO_CARGA)
    statusS1000 = False
    statusS1000 = s1000.mapear();

    assert statusS1000 == False
