from desafio026 import *

def main():

    f1 = Horista('Caio Luiz', 25, 250)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = Mensalista('Giovanna Ribeiro', 5000)
    f2.calc_sal()
    f2.analisar_sal()

if __name__ == '__main__':
    main()
