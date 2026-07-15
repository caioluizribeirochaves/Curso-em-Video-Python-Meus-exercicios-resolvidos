from functools import singledispatchmethod

class Analisador:
    @singledispatchmethod
    def Analisar(self, valor):
        print(f'Não foi possível analisar {valor}')

    @Analisar.register
    def _(self, valor:int):
        print(f'{valor} é um número inteiro')

    @Analisar.register
    def _(self, valor:float):
        print(f'{valor} é um número real')

    @Analisar.register
    def _(self, valor:str):
        print(f'{valor} é uma cadeia de caracteres')

    @Analisar.register
    def _(self, valor: tuple|dict|list):
        print(f'{valor} é uma coleção de dados')