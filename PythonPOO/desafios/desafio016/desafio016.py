# Crie a classe funcionário, onde podemos cadastrar nome, setor e cargo. Crie também um método que permita ao funcionário se apresentar.
from rich import print
from rich import inspect

class Funcionario:
    empresa = 'Curso em Vídeo'
    def __init__(self, nome='<Desconhecido>', setor='<Desconhecido>', cargo='<Desconhecido>'):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}.'


c1 = Funcionario('Caio', 'TI', 'Funcionário')
print(c1.apresentar())
# print(c1.__dict__)
# inspect(c1, methods=True, dunder=True)

c2 = Funcionario('Giovanna', 'TI', 'Funcionária')
print(c2.apresentar())
# print(c2.__dict__)
# inspect(c2, methods=True, dunder=True)
