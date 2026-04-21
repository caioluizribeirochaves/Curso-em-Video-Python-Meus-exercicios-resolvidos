# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint
from time import sleep
numeros = [ randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    sleep(0.5)
    for n in numeros:
        print(n, end=' ')
        sleep(0.5)
    print('PRONTO!')
def somaPar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteia()
somaPar()

# Resolução Guanabara

def sortea(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for count in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


números = []
sortea(números)
somPar(números)