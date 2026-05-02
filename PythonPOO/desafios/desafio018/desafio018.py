# Crie a classe Churrasco, onde seja possível informar quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.
# Considere:
# Consumo padrão: 400g por pessoa
# Preço: R$82,40/kg
from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self,titulo, quantidade=0):
        self.titulo = titulo
        self.quantidade = quantidade

    def calculo(self):
        return self.quantidade * 0.4

    def custo(self):
        return self.calculo() * 82.40

    def custopessoa(self):
        return self.custo() / self.quantidade

    def analisar(self):
        titulo = self.titulo
        dados = f'Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/]'
        dados += '\nCada Participante comerá 0.4Kg e cada Kg Custa R$82.40'
        dados += f'\nRecomendo [blue]comprar {self.calculo():.3f}Kg[/] de carne'
        dados += f'\nO custo total será de [green]R${self.custo():.2f}[/]'
        dados += f'\nCada pessoa pagará [yellow]R${self.custopessoa()}[/] para participar.'
        return Panel(dados, title=titulo)


c1 = Churrasco('Churras dos Brothers', 10)
print(c1.analisar())

c2 = Churrasco('Churras dos Amigos', 15)
print(c2.analisar())

#
#
# from rich import print
# from rich.table import Table
#
#
# class Churrasco:
#     preco_carne:float = 82.4 #82,4R$/kg
#     kg_carne_pessoa:float = 0.4 #400g/pessoa
#
#
#     def __init__(self, titulo, pessoas):
#         self.title=titulo
#         self.people=pessoas
#
#
#     def carne(self):
#         total_carne = self.people * Churrasco.kg_carne_pessoa
#         total_churras = total_carne * self.__class__.preco_carne
#         preco_pessoa = total_churras/self.people
#         #return (f" O total de carne será {total_carne} Kgs e o valor do churrasco é R$ {total_churras} \n "
#                 #f"Para {self.people} pessoas, o valor do churrasco é R$ {preco_pessoa} cada")
#         tabela = Table(title=f"[bold red]{self.title}".center(30), width=80,style='blue',)
#         tabela.add_column(f"[yellow]Qtd. Pessoas",justify="center", width= 7, style='green')
#         tabela.add_column("[yellow]Total de Carne (Kg)",justify='center', width=12, style='green')
#         tabela.add_column("[yellow]Total do Churrasco (R$)",justify='center', width=14, style='green')
#         tabela.add_column("[yellow]Valor por Pessoa (R$)", justify='center', width=12, style='green')
#         tabela.add_row(f"{self.people}",
#                        f"{total_carne:.2f}".replace('.',','),
#                        f"{total_churras:.2f}".replace('.',','),
#                        f"{preco_pessoa:.2f}".replace('.',','))
#         print(tabela)
#
# churras1 = Churrasco("Churras dos Brothers", 15)
# churras2 = Churrasco("Aniversário Bombástico", 50)
# churras1.carne()
# churras2.carne()