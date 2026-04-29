# Declaração de classe:
class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade
    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = '<Desconhecido>', idade = 0): # Método construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1
        return f'{self.nome} fez aniversário e agora tem {self.idade} anos de idade'

    def __str__(self): # Dunder Method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

    def __getstate__(self):
        return f'Estado do objeto: nome = {self.nome} ; idade = {self.idade}'


# Declaração de objetos:
g1 = Gafanhoto('Caio',  27)
print(g1) # Mostra o nome e idade
print(g1.aniversario()) # Adiciona mais 1 na idade e mostra a mensagem
print(g1.__dict__) # Attribute
print(g1.__getstate__()) # Method
print(g1.__class__)
print(g1.__doc__) # Dunder Attribute


g2 = Gafanhoto('Geraldo', 55)
print(g2)
print(g2.__getstate__())