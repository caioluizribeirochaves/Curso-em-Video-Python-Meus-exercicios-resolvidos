class Avaliacao:

    def __init__(self, nome, materia, nota=0):
        self.nome = nome
        self.materia = materia
        self._nota = nota

    # MÉTODOS ASSESSORES
    def get_nota(self): # Metodo Getter
        return self._nota

    def set_nota(self, valor): # Metodo Setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('Nota inválida')
