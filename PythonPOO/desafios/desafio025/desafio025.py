from abc import ABC, abstractmethod


class Transporte(ABC):

    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        self.frete = self.distancia * Moto.fator
        return f'R${self.frete:.2f}'

class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)  # min 50km

    def calc_frete(self):
        if self.distancia < 50:
            self.frete = 0
            return 'Distância mínima de 50Km'
        else:
            self.frete = self.distancia * Caminhao.fator
            return f'R${self.distancia * Caminhao.fator:.2f}'

class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia) # max 10km

    def calc_frete(self, fator=None):
        if self.distancia > 10:
            self.frete = 0
            return 'Distância máxima de 10Km'
        else:
            self.frete = self.distancia * Drone.fator
            return f'R${self.distancia * Drone.fator:.2f}'
