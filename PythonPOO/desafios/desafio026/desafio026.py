from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self, nome='<Desconhecido>', sal_bruto=0, salario=0):
        self.nome = nome
        self.bruto = sal_bruto
        self.salario = salario
        self.salario_min = 1612
        self.inss = 7.5

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        pass

class Horista(Funcionario):

    def __init__(self, nome, sal_bruto, salario, valor_horas, horas_trab):
        super().__init__(nome, sal_bruto, salario)
        self.valor_hora = valor_horas
        self.horas_trab = horas_trab

    def calc_sal(self):
        pass

class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto, salario):
        super().__init__(nome, sal_bruto, salario)

    def calc_sal(self):
        pass
