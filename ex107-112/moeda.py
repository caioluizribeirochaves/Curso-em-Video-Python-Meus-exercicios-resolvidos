# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
def aumentar(preço=0, taxa=0):
    """Calcula o preço aumentando a taxa percentual"""
    res = preço + (preço * taxa / 100)
    return res


def diminuir(preço=0, taxa=0):
    """Calcula o preço diminuindo a taxa percentual"""
    res = preço - (preço * taxa / 100)
    return res


def dobro(preço=0):
    """Calcula o dobro do preço"""
    res = preço * 2
    return res


def metade(preço=0):
    """Calcula a metade do preço"""
    res = preço / 2
    return res


# Exercício 108
def form(preço=0, moeda='R$'):
    """Formata o preço para o formato monetário"""
    res = f'{moeda}{preço:.2f}'.replace('.', ',')
    return res
