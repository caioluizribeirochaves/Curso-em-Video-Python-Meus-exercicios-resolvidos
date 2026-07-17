from ex015 import *

def main():

    c1 = Carteira(100)
    c2 = Carteira(100)
    c1 += 100

    if (c1 <= c2):
        print('A primeira carteira tem mais dinheiro')
    else:
        print('A segunda carteira tem mais dinheiro')

    if (c1 == c2):
        print('Vocês tem o mesmo valor na carteira')
    else:
        print('As carteiras tem valores diferentes')

    print(c1)
    print(c2)

if __name__ == '__main__':
    main()