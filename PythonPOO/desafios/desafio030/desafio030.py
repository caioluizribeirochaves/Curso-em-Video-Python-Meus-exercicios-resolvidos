# Crie uma classe que gerencie a has SHA256 de uma senha.
# Class Credencial
# Atributos:
# @senha
# __hash
# Métodos:
# validar(chave)
from hashlib import sha256

class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave):
        if len(chave) >= 8:
            self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        else:
            raise ValueError('Senha Inválida! Deve conter pelo menos 8 caracteres.')

    def validar(self, chave):
        validar = sha256(chave.encode('utf-8')).hexdigest()
        if validar == self.__hash:
            print('Senha Válida!')
            return True
        else:
            print('Senha Inválida!')
            return False
