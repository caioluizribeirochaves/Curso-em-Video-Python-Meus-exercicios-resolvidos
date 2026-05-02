# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5.
# E peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
print('-=-' * 12)
print('Vou pensar em um número entre 0 e 5.')
print('-=-' * 12)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
numr = [0, 1, 2, 3, 4, 5]
random.choice(numr)
if random.choice(numr) == num:
    print('Parabéns! Você acertou!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}, tente novamente!' .format(random.choice(numr), num))

# Resolução do Guanabara:
# from random import randint
# from time import sleep
# computador = randint(0, 5) # Faz o computador "pensar"
# print('-=-' * 20)
# print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
# print('-=-' * 20)
# jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
# print ('PROCESSANDO...')
# sleep(2)
# if jogador == computador:
#   print('Parabéns! Você conseguiu me vencer!')
# else:
#   print('Ganhei! Eu pensei no número {} e não no {}, tente novamente!' .format(computador, jogador))