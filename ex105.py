# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação(opcional)
# Adicione também as docstrings da função.
def nota(*n, sit=False):
    """
    -> Função para analisar notas e situação de muitos alunos.
    :param n: Notas dos alunos
    :param sit: (Opcional) Se deve ou não mostrar a situação que a turma se encontra
    :return: Retorna com o total de notas, a maior nota, a menor nota e a média da turma, inclusive a situação que é opcional
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Média'] >= 5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'
    return r


resp = nota(2, 2, 9, 4, 5, sit=True)
print(resp)
help(nota)