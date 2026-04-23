# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
# Exercício 109 é "formatar=False" e "return res if formatar is False else form(res)"
def aumentar(preço=0, taxa=0, formatar=False):
    """Calcula o preço aumentando a taxa percentual"""
    res = preço + (preço * taxa / 100)
    return res if formatar is False else form(res)


def diminuir(preço=0, taxa=0, formatar=False):
    """Calcula o preço diminuindo a taxa percentual"""
    res = preço - (preço * taxa / 100)
    return res if formatar is False else form(res)


def dobro(preço=0, formatar=False):
    """Calcula o dobro do preço"""
    res = preço * 2
    return res if formatar is False else form(res)


def metade(preço=0, formatar=False):
    """Calcula a metade do preço"""
    res = preço / 2
    return res if formatar is False else form(res)


# Exercício 108
def form(preço=0, moeda='R$'):
    """Formata o preço para o formato monetário"""
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


# Exercício 110
def resumo(preço=0, taxa_aum=10, taxa_dim=5):
    """Mostra um resumo das principais funções da moeda.py"""
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{form(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxa_aum}% de aumento: \t{aumentar(preço, taxa_aum, True)}')
    print(f'{taxa_dim}% de redução: \t{diminuir(preço, taxa_dim, True)}')
    print('-' * 30)
    