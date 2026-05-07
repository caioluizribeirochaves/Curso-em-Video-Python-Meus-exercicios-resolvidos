from math import pi
from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados=0):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Circulo(Poligono):
    def __init__(self, raio=0, qtd_lados=0) :
        super().__init__(qtd_lados)
        self.raio = raio

    def perimetro(self):
        return 2 * pi * self.raio

    def area(self):
        return pi * self.raio ** 2

class Quadrado(Poligono):
    def __init__(self, lado=0, qtd_lados=4):
        super().__init__(qtd_lados)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2