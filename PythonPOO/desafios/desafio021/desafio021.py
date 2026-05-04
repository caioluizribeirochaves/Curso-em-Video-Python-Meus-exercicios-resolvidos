# Crie a classe Caneta, que simule o funcionamento de uma caneta colorida, podendo escrever frases na cor relativa.
from rich import print

class Caneta:
    def __init__(self, cor='azul'):
        escolha = ''
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]'
            case 'verde':
                escolha = '[green]'
            case _:
                escolha = '[white]'
        self.cor = escolha
        self.tampada = True

    def escrever(self, msg):
        if self.tampada:
            print(f':prohibited: A {self.cor}caneta[/] está tampada!')
        else:
            print(f'{self.cor}{msg}[/]', end='')

    def quebrar_linha(self, qtd=1):
        print('\n' * qtd, end='')

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('verde')
c1.destampar()
c2.destampar()
c3.destampar()
c1.escrever('Olá Mundo!')
c2.escrever('Tudo certo?')
c3.escrever('Estou aprendendo muita coisa massa!')