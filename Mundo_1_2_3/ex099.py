# Faça um programa que tenha uma função chamada maior(), que receba varios parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def valores(*valor):
    maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for v in valor:
        if v > maior:
            maior = v
    for v in valor:
        print(f'{v} ', end='')
        sleep(0.25)
    print(f'Foram informados {len(valor)} ao todo.')
    print(f'O maior valor informado foi {maior}')


valores(2, 5, 10, 20, 12, 4)
valores(4, 6, 7, 8, 9, 10)
valores(1, 2, 3, 4, 5, 6)
valores()