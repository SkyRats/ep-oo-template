import sys
sys.path.append('../scripts')

from s1000 import S1000

def test_construtor():
    CAPACIDADE_MAH = 22000
    TEMPO_CARGA = 40
    POS_S1000 = 0
    ALTURA_S1000 = 10
    NOME_S1000 = "S1000"
    batS1000 = Bateria(CAPACIDADE_MAH, TEMPO_CARGA)
    s1000 = S1000(NOME_S1000, batS1000, POS_S1000)

    assert s1000._nome == NOME_S1000
    assert s1000._posicao == POS_S1000

def test_mapear():
    CAPACIDADE_MAH = 22000
    TEMPO_CARGA = 40
    POS_S1000 = 0
    ALTURA_S1000 = 10
    NOME_S1000 = "S1000"
    batS1000 = Bateria(CAPACIDADE_MAH, TEMPO_CARGA)
    s1000 = S1000(NOME_S1000, batS1000, POS_S1000)

    statusS1000 = False
    batS1000.carregar(TEMPO_CARGA)
    s1000.takeoff(ALTURA_S1000)
    statusS1000 = s1000.mapear()

    assert statusS1000 == True

def test_mapearSemBateria():
    CAPACIDADE_MAH = 22000
    TEMPO_CARGA = 40
    POS_S1000 = 0
    ALTURA_S1000 = 10
    NOME_S1000 = "S1000"
    batS1000 = Bateria(CAPACIDADE_MAH, TEMPO_CARGA)
    s1000 = S1000(NOME_S1000, batS1000, POS_S1000)

    statusS1000 = False
    s1000.takeoff(ALTURA_S1000)
    statusS1000 = s1000.mapear();

    assert statusS1000 == False

def test_mapearSemTakeoff():
    CAPACIDADE_MAH = 22000
    TEMPO_CARGA = 40
    POS_S1000 = 0
    ALTURA_S1000 = 10
    NOME_S1000 = "S1000"
    batS1000 = Bateria(CAPACIDADE_MAH, TEMPO_CARGA)
    s1000 = S1000(NOME_S1000, batS1000, POS_S1000)

    batS1000.carregar(TEMPO_CARGA)
    statusS1000 = False
    statusS1000 = s1000.mapear();

    assert statusS1000 == False
