# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
geral = {}
geral['Nome'] = str(input('Nome: ')).strip().capitalize()
geral['Idade'] = date.today().year - int(input('Ano de nascimento: '))
geral['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if geral['CTPS'] != 0:
    geral['Contratação'] = int(input('Ano de contratação: '))
    geral['Salaário'] = float(input('Salário: R$'))
    carteira = date.today().year - geral['Contratação']
    geral['Aposentadoria'] = (35 - carteira) + geral['Idade']
print('-=' * 30)
for k, v in geral.items():
    print(f' - {k} tem o valor \033[32m{v}\033[m.')
