class Bateria():
    def __init__(self, mah, tempoDeCarregamento):
        raise NotImplementedError
        
    def carregar(self, tempo):
        raise NotImplementedError

    def usar(self, tempo):
        raise NotImplementedError

    def getCarga(self):
        raise NotImplementedError

    def getTempoDeVoo(self):
        raise NotImplementedError

    def status(self):
        raise NotImplementedError

class Drone():
    def __init__(self, nome, bateria, posicao):
        raise NotImplementedError

    def takeoff(self, altura):
        raise NotImplementedError
        
    def land(self):
        raise NotImplementedError

    def set_position(self, x, y):
        raise NotImplementedError

    def mapear(self):
        raise NotImplementedError

    def status(self):
        raise NotImplementedError

class S1000():
    def __init__(self, nome, bateria, posicao):
        raise NotImplementedError
