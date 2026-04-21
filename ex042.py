# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#  - Equilátero: todos os lados iguais
#  - Isósceles: dois lados iguais
#  - Escaleno: todos os lados diferentes
from time import sleep
print('-=-' * 11)
print('É possível formar um triângulo?')
print('-=-' * 11)
l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))
print('PROCESSANDO...')
sleep(2)
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('É possível formar um TRIÂNGULO')
    if l1 == l2 == l3:
        print('E esse TRIÂNGULO é EQUILATERO')
    elif l1 != l2 != l3 != l1:
        print('E esse TRIÂNGULO é ESCALENO')
    elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
        print('E esse TRIÂNGULO é ISÓSCELES')
else:
    print('Não é possível formar um TRIÂNGULO')