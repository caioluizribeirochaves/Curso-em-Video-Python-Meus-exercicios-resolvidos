from desafio033 import *

def main():
    a = Aluno('Caio', 1999, 'ADS')

    a.add_curso('MODA')

    print(a.cursos_oficiais)
    print(a.__dict__)


if __name__ == '__main__':
    main()