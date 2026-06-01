from desafio032 import *

def main():

    cc = ContaBancaria(123, 'Caio', 10_000)
    cc.depositar(500)
    cc.sacar(1000)
    cc.nome = 'Giovanna'
    print(cc)

if __name__ == '__main__':
    main()