from desafio034 import *

def main():
    funcionarios = [
        Desenvolvedor("Caio", 20_000),
        Designer("Gislene", 25_000),
        Gerente("Geraldo", 30_000)
    ]

    for f in funcionarios:
        print(f)

if __name__ == '__main__':
    main()