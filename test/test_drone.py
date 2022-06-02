import sys
sys.path.append('../scripts')

import pytest
from helper import get_attr
from drone import Drone
from bateria import Bateria

CAPACIDADE = 1000
TEMPO_CARGA = 10
BATERIA = None

NOME = "Nome_teste"
POSICAO = 0
DRONE = None

ALTURA_DECOLAGEM = 2.0
POSICAO_SET_POSITION = 10

@pytest.fixture(autouse=True)
def reseta_drone():
    global DRONE
    global BATERIA
    BATERIA = Bateria(CAPACIDADE, TEMPO_CARGA)
    DRONE = Drone(NOME, BATERIA, POSICAO)

def test_construtor():
    assert get_attr(DRONE, 'nome') == NOME
    assert get_attr(DRONE, 'altura') == 0.0
    assert get_attr(DRONE, 'decolado') == False

def modulo(deltaX, deltaY):
    return (deltaX**2 + deltaY**2)**0.5

def cargaUsada(distancia):
    return (1000 * distancia/60) / 10

def test_takeoff():
    get_attr(DRONE, 'bateria').carregar(TEMPO_CARGA)
    DRONE.takeoff(ALTURA_DECOLAGEM)
    assert get_attr(DRONE, 'altura') == ALTURA_DECOLAGEM

def test_land():
    get_attr(DRONE, 'bateria').carregar(TEMPO_CARGA)
    cargaAntesDoLand = get_attr(BATERIA, 'carga')

    assert get_attr(DRONE, 'decolado') == False
    assert get_attr(DRONE, 'altura') == 0
    DRONE.takeoff(ALTURA_DECOLAGEM)
    assert get_attr(DRONE, 'altura') == ALTURA_DECOLAGEM

def test_setPositionSemDecolar():
    DRONE.land()
    assert DRONE.set_position(0, 0) == False

def test_setPositionPrimeiroQuadrante():
    get_attr(DRONE, 'bateria').carregar(TEMPO_CARGA)
    DRONE.takeoff(ALTURA_DECOLAGEM)
    DRONE.set_position(POSICAO_SET_POSITION, ALTURA_DECOLAGEM)
    assert get_attr(DRONE, 'posicao') > 0

def test_setPositionQuartoQuadrante():
    get_attr(DRONE, 'bateria').carregar(TEMPO_CARGA)
    DRONE.takeoff(ALTURA_DECOLAGEM)
    assert DRONE.set_position(POSICAO_SET_POSITION, -ALTURA_DECOLAGEM) == False

def test_setPositionAlturaNula():
    assert DRONE.set_position(POSICAO_SET_POSITION, 0) == False

def test_setPositionSegundoQuadrante():
    DRONE.takeoff(ALTURA_DECOLAGEM)
    DRONE.set_position(-POSICAO_SET_POSITION, ALTURA_DECOLAGEM)
    assert get_attr(DRONE, 'posicao') == 0

def test_mapear():
    DRONE.land()
    assert DRONE.mapear() == False
    DRONE.takeoff(ALTURA_DECOLAGEM)
    assert DRONE.mapear() == False
