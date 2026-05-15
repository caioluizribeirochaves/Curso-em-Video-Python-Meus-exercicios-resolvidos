from desafio028 import *
from rich import print, inspect

def main():

    t = Termostato()
    try:
        t.temperatura = 23.2
    except Exception as e: # vai puxar o valueError, sendo representado pela letra 'e'
        print(f'Houve um problema: {e}')

    print(f'A temperatura atual é de {t.ftemperatura}')
    # inspect(t,  methods=True)


if __name__ == '__main__':
    main()