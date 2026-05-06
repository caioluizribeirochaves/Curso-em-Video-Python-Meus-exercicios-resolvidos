from rich import print, inspect
from classes import Pessoa, Aluno, Professor, Funcionario

def main():
    a1 = Aluno('Caio', 27, 'ADS', 'EAD')
    a1.fazer_aniversario()
    a1.fazer_matricula()
    a1.estudar()
    inspect(a1, methods=True)

    p1 = Professor('Guanabara', 55, 'Sabe Tudo', 'GOD')
    p1.dar_aula()
    p1.estudar()
    inspect(p1, methods=True)

    f1 = Funcionario('Creuza', 67, 'RH', 'Senior')
    f1.bater_ponto()
    f1.estudar()
    inspect(f1, methods=True)


if __name__ == '__main__':
    main()
