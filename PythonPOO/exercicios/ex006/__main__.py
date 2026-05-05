from rich import print, inspect
from Aluno import Aluno
from Professor import Professor
from Funcionario import Funcionario

def main():
    a1 = Aluno('Caio', 27, 'ADS', 'EAD')
    a1.fazer_aniversario()
    a1.fazer_matricula()
    inspect(a1, methods=True)

    p1 = Professor('Guanabara', 55, 'Sabe Tudo', 'GOD')
    p1.dar_aula()
    inspect(p1, methods=True)

    f1 = Funcionario('Creuza', 67, 'RH', 'Senior')
    f1.bater_ponto()
    inspect(f1, methods=True)


if __name__ == '__main__':
    main()
