class Numero:

    def __init__(self, valor: int|float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor = self.valor * 2

    def __str__(self):
        return f'O valor número informado foi {self.valor}'

class Papel:

    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__(self):
        return f'O papel está {'novo' if not self.dobrado else 'dobrado'}'

class Casa:

    def __init__(self):
        pass

    def __str__(self):
        return 'Não tinha teto, não tinha nada...'

def tentar_dobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f'Tive dificuldades de dobra {objeto.__class__.__name__}')