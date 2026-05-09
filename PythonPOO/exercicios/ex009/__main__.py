from ex009 import *
from rich import print, inspect

def main():

    av1 = Avaliacao('Caio', 'Programação')
    av1.set_nota(5)
    print(f'{av1.nome} tirou {av1.get_nota()} em {av1.materia}')
    # inspect(av1, private=True)

if __name__ == "__main__":
    main()