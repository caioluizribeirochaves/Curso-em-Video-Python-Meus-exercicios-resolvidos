from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init(self, distancia=0, frete=0):
        self.distancia = distancia
        self.frete = frete

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.distancia = distancia
        self.frete  #Livre
        self.fator = 0.50

    def calc_frete(self):

class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.distancia = distancia
        self.frete  #min 50km
        self.fator = 1.20

    def calc_frete(self):

class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.distancia = distancia
        self.frete  #max 10km
        self.fator = 9.50

    def calc_frete(self):
