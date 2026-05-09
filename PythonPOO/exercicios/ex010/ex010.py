class Avaliacao:

    def __init__(self, nome, materia, nota=0):
        self.nome = nome
        self.materia = materia
        self._nota = nota

    # Atributos Validáveis @getter @setter @deleter
    @property
    def nota(self): # Getter
        return self._nota

    @nota.setter
    def nota(self, valor): # Setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('Nota inválida')

