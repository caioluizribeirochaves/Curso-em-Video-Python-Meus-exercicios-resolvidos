class Mae:
    def __init__(self, nome:str =''):
        self.nome = nome

    def fazer_pudim(self):
        print(f'{self.nome} fez um PUDIM com leite condensado e calda de açucar')

    def fritar_coxinha(self):
        print(f'{self.nome} fez uma COXINHA no óleo de soja')

class Filho(Mae):
    def fritar_coxinha(self):
        print(f'{self.nome} fez uma COXINHA na airfryer')

class Filha(Mae):
    def fazer_pudim(self):
        print(f'{self.nome} fez um PUDIM de Leite em pó com calda de avelã')

