# Crie a classe Gamer, onde podemos cadastrar, nome, nick e os jogos favoritos de uma pessoa.
# Crie também um método que permita mostrar a ficha desse gamer.
from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome='<Desconhecido>', nick='<Desconhecido>'):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        dados = (f'Nome real: [black on blue]{self.nome}[/]')
        dados += (f'\nJogos favoritos:')
        for num, game in enumerate(self.favoritos):
            dados += f'\n:video_game: [blue]{game}[/]'
        painel = Panel(dados, title=f'Jogador <[bold]{self.nick}[/]>', width=40)
        print(painel)



j1 = Gamer('Caio Luiz', 'Caiebas')
j1.add_favoritos('God Of war')
j1.add_favoritos('Crash Bandicoot')
j1.ficha()

