# A confraternização Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#  - Até 9 anos: MIRIM
#  - Até 14 anos: INFANTIL
#  - Até 19 anos: JUNIOR
#  - Até 20 anos: SÊNIOR
#  - Acima: MASTER
from datetime import date
anoatual = date.today().year
anonasc = int(input('Digite o ano de nascimento: '))
idade = anoatual - anonasc
print('Você nasceu em {}, tem {} anos.' .format(anonasc, idade))
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade <= 25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
