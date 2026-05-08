from desafio027 import *

def main():

    p1 = Guerreiro('Megaman', 1000)
    p2 = Mago('Merlim', 2000)
    p3 = Guerreiro('Kratos', 1500)

    p1.atacar(p2, 200)
    p3.atacar(p1, 300)
    p2.atacar(p3, 150)

    p1.curar()
    p2.curar()

if __name__ == '__main__':
    main()