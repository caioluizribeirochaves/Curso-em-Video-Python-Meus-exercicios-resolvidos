# Crie uma classe livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou no fim da leitura
from turtledemo.round_dance import stop

from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo='<Desconhecido>', paginas=0):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1

        print(f':open_book: [blue]Você acabou de abrir o livro [red]{self.titulo}[/] que tem [green]{self.paginas} paginas[/] no total. Você agora está na [yellow]página {self.pagina_atual}[/][/]')

    def avancar_paginas(self, qtd=0):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f'Pág{self.pagina_atual} :arrow_forward:', end=' ')
                sleep(0.3)
                cont += 1
        print(f'[blue]Você avançou [bold]{qtd}[/] páginas e agora está na [yellow]página {self.pagina_atual}[/]')
        if self.fim_do_livro():
            print(f':closed_book: [red]Você chegou ao final do livro [bold]{self.titulo}[/][/]')

    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.paginas else False


l1 = Livro('10 coisas que aprendi', 20)
l1.avancar_paginas(3)
l1.avancar_paginas(30)