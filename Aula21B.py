# Escopo de variáveis


def local(b):
    """
    :param global a: valor da variavel de fora, vai ser refletido no valor do a de dentro
    :param b: valor da variável informada do lado de fora
    :return: sem retorno
    """
    global a
    a = 5
    b += 4
    c = 2
    print(f'O a dentro vale {a} ')
    print(f'O b dentro vale {b} ')
    print(f'O c dentro vale {c} ')


a = 3
local(5)
print(f'O a fora vale {a}')
