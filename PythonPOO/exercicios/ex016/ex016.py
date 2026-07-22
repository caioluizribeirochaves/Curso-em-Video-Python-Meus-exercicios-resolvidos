class ovo:
    def abrir(self):
        print(f"Quebra a casca com um garfo e separe as partes sobre uma frigideira")

class Pedra:
    pass


def tentar_abri(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Encontrei problemas ao tentar abrir um objeto tipo {objeto.__class__.__name__}")