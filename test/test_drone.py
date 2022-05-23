import sys
sys.path.append('../scripts')

from drone import Drone
from bateria import Bateria

def modulo(deltaX, deltaY):
    return (deltaX**2 + deltaY**2)**0.5

def cargaUsada(distancia):
    return (1000 * distancia/60) / 10

def test_construtor():
    CAPACIDADE_MAH = 1000
    TEMPO_CARGA = 10
    POS_INICIAL = 5.0
    NOME = "Robinho"
    bateria = bateria(CAPACIDADE_MAH, TEMPO_CARGA)
    drone = drone(NOME, bateria, POS_INICIAL)

    assert drone._nome == NOME
    assert drone._posicao == POS_INICIAL


def test_takeoff():
    pass

def test_land():
    CAPACIDADE_MAH = 1000
    TEMPO_CARGA = 10
    ALTURA_DECOLAGEM = 3
    POS_INICIAL = 5.0
    NOME = "Robinho"
    bateria = bateria(CAPACIDADE_MAH, TEMPO_CARGA)
    drone = drone(NOME, bateria, POS_INICIAL)

    bateria._carregar(TEMPO_CARGA)
    drone.takeoff(ALTURA_DECOLAGEM)
    cargaAntesDoLand = bateroa._carga

    assert bateria._carga == cargaAntesDoLand
    assert drone._decolado == False
    assert drone._altura == 0
    assert bateria._carregavel == True

def test_setPositionSemDecolar():
    pass

def test_setPositionPrimeiroQuadrante():
    pass

def test_setPositionQuartoQuadrante():
    pass

def test_setPositionAlturaNula():
    pass

def test_setPositionSegundoQuadrante():
    pass

def test_mapear():
    CAPACIDADE_MAH = 1000
    TEMPO_CARGA = 10
    ALTURA_DECOLAGEM = 3
    POS_INICIAL = 5.0
    NOME = "Robinho"
    bateria = bateria(CAPACIDADE_MAH, TEMPO_CARGA)
    drone = drone(NOME, bateria, POS_INICIAL)

    assert mapear == False
