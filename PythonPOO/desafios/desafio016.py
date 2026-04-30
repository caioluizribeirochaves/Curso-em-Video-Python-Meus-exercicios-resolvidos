# Crie a classe funcionário, onde podemos cadastrar nome, setor e cargo. Crie também um método que permita ao funcionário se apresentar.
from rich import print

class Funcionario:
    def __init__(self, nome='<Desconhecido>', setor='<Desconhecido>', cargo='<Desconhecido>'):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa.'


c1 = Funcionario('Caio', 'TI', 'Funcionário')
print(c1.apresentar())

c2 = Funcionario('Giovanna', 'TI', 'Funcionária')
print(c2.apresentar())
