# Declaração de classe:
class Gafanhoto:
    def __init__(self): # Método construtor
        # Atributos de Instância
        self.nome = ''
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1
        return f'{self.nome} fez aniversário e agora tem {self.idade} anos de idade'

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

# Declaração de objetos:
g1 = Gafanhoto()
g1.nome = 'Caio'
g1.idade = 27
print(g1.mensagem())
print(g1.aniversario())
