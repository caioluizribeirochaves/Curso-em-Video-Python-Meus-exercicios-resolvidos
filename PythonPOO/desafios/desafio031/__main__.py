from desafio031 import *

def main():
    r = Retangulo()
    try:
        r.medidas = (4, 5)
        print(r.medidas)
    except Exception as e:
        print(f'Ocorreu um erro do tipo {type(e).__name__}: {e}')


if __name__ == '__main__':
    main()