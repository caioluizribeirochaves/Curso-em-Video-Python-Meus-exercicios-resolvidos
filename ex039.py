# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
#  - Se ele ainda vai se alistar ao serviço militar.
#  - Se é a hora de se alistar.
#  - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
anonasc = int(input('Ano de nascimento: '))
anoatual = date.today().year
alistam = anoatual - anonasc
if alistam < 18:
    print('Você nasceu em {}, tem {} anos em {}. \nDeve se alistar daqui {} ano(s).' .format(anonasc, alistam, anoatual, 18 - alistam))
    print('Aguardamos seu retorno')
elif alistam == 18:
    print('Você nasceu em {}, tem {} anos em {}, \ndeve se alistar agora!' .format(anonasc, alistam, anoatual))
    print('Compareça a uma junta militar!')
else:
    print('Você nasceu em {}, tem {} anos em {}, \nexcedeu o prazo de alistamento em {} ano(s).' .format(anonasc, alistam, anoatual, alistam - 18))
    print('Compareça a uma junta militar para regularizar seu débito.')
