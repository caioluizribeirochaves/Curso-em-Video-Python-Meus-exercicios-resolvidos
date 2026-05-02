# Docstrings e interactive help

from time import sleep
def contador(i, f, p):
    """
    > Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Caio Luiz Ribeiro Chaves
    """
    c = i
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    while c <= f:
        print(f'{c}', end='..')
        sleep(0.3)
        c += p
    print('FIM')


contador(1, 100, 5)
help(contador)

# Argumentos opcionais


def somar(a=0, b=0, c=0):
    """
    > Faz uma soma e mostra na tela o resultado
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem retorno
    Função criada por Caio Luiz Ribeiro Chaves
    """
    somas = a + b + c
    print(f'A soma vale {somas}')


somar(10, 4, 9)
somar(2, 7)
somar()
help(somar)


def soma(*num):
    """
    > Faz uma soma entre variáveis valores e mostra na tela a soma
    :param num: recebe a lista de valores digitados
    :return: sem retorno
    """
    somares = sum(num)
    print(f'A soma vale {somares}')


soma(10, 4, 9)
soma(2, 7)
soma()
help(soma)