# Crie um programa que tenha uma função chamada fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e o outro chamado show,
# que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(n, show=False):
    """
    -> Retorna o fatorial de um número
    :param n: número a ser fatorado
    :param show: (opcional) Mostra o calculo do fatorial
    :return: retorna o fatorial do número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
print(help(fatorial))
