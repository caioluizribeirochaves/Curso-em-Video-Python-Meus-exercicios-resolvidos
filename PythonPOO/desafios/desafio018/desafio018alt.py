from rich import print
from rich.table import Table


class Churrasco:
    preco_carne:float = 82.4 #82,4R$/kg
    kg_carne_pessoa:float = 0.4 #400g/pessoa


    def __init__(self, titulo, pessoas):
        self.title=titulo
        self.people=pessoas


    def carne(self):
        total_carne = self.people * Churrasco.kg_carne_pessoa
        total_churras = total_carne * self.__class__.preco_carne
        preco_pessoa = total_churras/self.people
        #return (f" O total de carne será {total_carne} Kgs e o valor do churrasco é R$ {total_churras} \n "
                #f"Para {self.people} pessoas, o valor do churrasco é R$ {preco_pessoa} cada")
        tabela = Table(title=f"[bold red]{self.title}".center(30), width=80,style='blue',)
        tabela.add_column(f"[yellow]Qtd. Pessoas",justify="center", width= 7, style='green')
        tabela.add_column("[yellow]Total de Carne (Kg)",justify='center', width=12, style='green')
        tabela.add_column("[yellow]Total do Churrasco (R$)",justify='center', width=14, style='green')
        tabela.add_column("[yellow]Valor por Pessoa (R$)", justify='center', width=12, style='green')
        tabela.add_row(f"{self.people}",
                       f"{total_carne:.2f}".replace('.',','),
                       f"{total_churras:.2f}".replace('.',','),
                       f"{preco_pessoa:.2f}".replace('.',','))
        print(tabela)

churras1 = Churrasco("Churras dos Brothers", 15)
churras2 = Churrasco("Aniversário Bombástico", 50)
churras1.carne()
churras2.carne()