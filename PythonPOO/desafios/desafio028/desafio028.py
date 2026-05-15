# Similar um Termostato
# Atributos:
# __temperatura
# @temperatura
# @ftemperatura

class Termostato:
    def __init__(self, temp=24):
        self.__temperatura = temp

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError(f'Temperatura de {valor}{chr(176)} é inválida!') # Incrementa apenas de 0.5 em 0.5, não aceita outros valores como 22.2
        if valor > 30:
            self.__temperatura = 30
        elif valor < 16:
            self.__temperatura = 16
        else:
            self.__temperatura = valor

    @property
    def ftemperatura(self):
        return f'{self.__temperatura}{chr(176)}C' # chr(176) é o símbolo de graus
