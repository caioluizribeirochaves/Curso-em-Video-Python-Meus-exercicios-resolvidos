# Simule um Diário secreto orientado a objeto
# Diario
# atributos:
# __segredos[]
# __senha
# metodos:
# escrever(msg)
# ler(senha)
from rich import print

class Diario:
    def __init__(self, senha = '1234'):
        self.__segredos = []
        self.__senha = senha.strip()

    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0: # se a mensagem é uma string e o tamanho dela for maior do que 0, __segredos vai receber a mensagem
            self.__segredos.append(msg.strip())

    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError('Senha INVÁLIDA! Sai pra lá curioso...')
        else:
            print('[green]Diário LIBERADO! Oia só... :pleading_face: :point_down:[/]')
            for segredo in self.__segredos:
                print(f'[magenta]- {segredo}[/]')

    @property
    def senha(self):
        raise PermissionError(f'Ninguém tem permissão de ver a senha!')

    @senha.setter
    def senha(self, novasenha = None):
        self.__senha = novasenha
