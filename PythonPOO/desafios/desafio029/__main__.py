from desafio029 import *
from rich import print, inspect

def main():

    d = Diario()
    d.senha = ''
    d.escrever('OLÁ MUNDO!')
    d.escrever('Estou testando isso aqui...')
    # d.senha = 'Caiebas'
    try:
        d.ler('')
    except Exception as e:
        print(f'[red]ERRO: {e}')
    # inspect(d, methods=True, private=True)


if __name__ == '__main__':
    main()