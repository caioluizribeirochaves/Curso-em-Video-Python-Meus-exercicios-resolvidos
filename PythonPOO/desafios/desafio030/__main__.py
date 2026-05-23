from desafio030 import *

def main():
    c = Credencial()
    try:
        c.senha = str(input('Digite a senha: '))
    except Exception as e:
        print(f'Ocorreu um erro do tipo {type(e).__name__}: {e}')
    print(c.senha)
    c.validar('Caiebas1234')


if __name__ == '__main__':
    main()