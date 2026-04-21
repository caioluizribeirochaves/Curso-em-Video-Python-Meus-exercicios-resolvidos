# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles
from time import sleep
print('*' * 46)
print('CONTAGEM REGRESSIVA PARA A QUEIMA DOS FOGOS!!!')
print('*' * 46)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('*' * 46)
print('{:=^46}' .format(' FELIZ ANO NOVO!!! '))
print('*' * 46)
