# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
from time import sleep
print('-' * 40)
print('É possível formar um triâgulo?')
print('-' * 40)
l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))
print('PROCESSANDO...')
sleep(2)
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')