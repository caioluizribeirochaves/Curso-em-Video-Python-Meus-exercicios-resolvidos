# Crie a classe Churrasco, onde seja possível informar quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.
# Considere:
# Consumo padrão: 400g por pessoa
# Preço: R$82,40/kg
from rich import print
from rich.panel import Panel

class Churrasco:
    # Atributo de Classe
    consumo_padrao = 0.400 # Cada pessoa come uma média de 400g de carne
    preco_kg = 82.40 # Cada Kg de carne custa R$82.40

    def __init__(self, titulo='<Não informado>', quantidade=0):
        self.titulo = titulo
        self.quantidade = quantidade

    def calculo(self) -> float:
        return self.quantidade * self.__class__.consumo_padrao # Posso usar também Churrasco.consumo_padrao

    def custo(self) -> float:
        return self.calculo() * self.__class__.preco_kg # Posso usar também Churrasco.preco_kg

    def custopessoa(self) -> float:
        return self.custo() / self.quantidade

    def analisar(self):
        dados = f'Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/]'
        dados += f'\nCada Participante comerá em média {Churrasco.consumo_padrao:.3f} gramas e cada Kg Custa R${Churrasco.preco_kg:.2f}'
        dados += f'\nRecomendo [blue]comprar {self.calculo():.3f}Kg[/] de carne'
        dados += f'\nO custo total será de [green]R${self.custo():.2f}[/]'
        dados += f'\nCada pessoa pagará [yellow]R${self.custopessoa()}[/] para participar.'
        painel = Panel(dados, title=self.titulo)
        return painel


c1 = Churrasco('Churras dos Brothers', 10)
print(c1.analisar())

c2 = Churrasco('Festa de Fim de Ano', 80)
print(c2.analisar())

