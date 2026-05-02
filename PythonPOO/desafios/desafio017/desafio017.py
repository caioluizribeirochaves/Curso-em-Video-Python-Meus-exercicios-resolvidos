# Crie a classe Produto, onde podemos cadastrar nome e preço. Crie também um método que mostre uma etiqueta de preço do produto.
from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome='<Desconhecido>', preco=0):
        self.produto = nome
        self.valor = preco

    def etiqueta(self):
        conteudo = f'{self.produto.center(30, ' ')}'
        conteudo += f'{'-' * 30}'
        valorf = f'R${self.valor:,.2f}'
        conteudo += f'{valorf.center(30, '.')}'
        return Panel(conteudo, title='Produto', width=34)

p1 = Produto('Monitor LG 34G600B-A', 2_000)
p2 = Produto('TV QN90F', 3_190)
p3 = Produto()

print(p1.etiqueta())
print(p2.etiqueta())
print(p3.etiqueta())
