from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):

    salario_min = 1612
    inss = 7.5

    def __init__(self, nome='<Desconhecido>'):
        self.nome = nome
        self.bruto = 0
        self.salario = 0


    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        base = self.salario/Funcionario.salario_min

        mensagem = f'O salário de [blue]{self.nome}[/] ([magenta]{self.__class__.__name__}[/]) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{base:.1f} salários mínimos[/]'
        painel = Panel(mensagem, title='Análise de salários', width=50)
        print(painel)


class Horista(Funcionario):

    def __init__(self, nome, valor_horas = 7.37, horas_trab = 200):
        super().__init__(nome)
        self.valor_hora = valor_horas
        self.horas_trab = horas_trab
        self.salario_bruto = self.valor_hora * self.horas_trab

    def calc_sal(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.inss/100)

class Mensalista(Funcionario):

    def __init__(self, nome, salario_bruto = Funcionario.salario_min):
        super().__init__(nome)
        self.salario_bruto = salario_bruto

    def calc_sal(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.inss/100)
