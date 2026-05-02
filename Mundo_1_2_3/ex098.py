# Faça um programa que tenha uma função chamada contador() que receba três parâmetros: início, fim e passo e realize a contagem
# Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada.
from time import sleep
def contagem(* valores):
    print('-=' * 30)
    print('Contagem de 1 até 10, em 1 em 1:')
    sleep(0.5)
    contador = 0
    while contador <= 10:
        print(contador, end= ' ')
        contador += 1
        sleep(0.5)
    sleep(0.5)
    print('FIM!')
    print('-=' * 30)
    print('Contagem de 10 até 0, de 2 em 2:')
    sleep(0.5)
    regressivo = 10
    while regressivo >= 0:
        print(regressivo, end=' ')
        regressivo -= 2
        sleep(0.5)
    sleep(0.5)
    print('FIM!')
    print('-=' * 30)
    print('Agora é sua vez de personalizar a contagem!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        while i <= f:
            print(i, end=' ')
            sleep(0.5)
            i += p
    elif i > f:
        while i >= f:
            print(i, end=' ')
            sleep(0.5)
            i -= p
    sleep(0.5)
    print('FIM!')
    print('-=' * 30)


contagem()
