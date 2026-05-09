from ex008 import *

def main():

    c1 = ContaBancaria(112, 'Caio', 150000)
    c1.depositar(-3500)
    c1.sacar(-2_000_000)
    c1.saldo = 2
    print(c1)


if __name__ == '__main__':
    main()