# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
ano = int(input('Em que ano estamos? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano {} é BISSEXTO!' .format(ano))
else:
    print('Esse ano {} NÃO é BISSEXTO!' .format(ano))
