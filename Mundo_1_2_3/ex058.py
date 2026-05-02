# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
computador = randint(0, 10)
jogador = 0
tentativas = 0
print('-=-' * 12)
print('        JOGO DA ADIVINHAÇÃO')
print('-=-' * 12)
sleep(1)
print('Vou pensar em um número entre 0 e 10...')
sleep(1)
print('Tente adivinhar...')
sleep(1)
while jogador != computador:
    jogador = int(input('Qual número eu pensei? '))
    print('PROCESSANDO...')
    sleep(1)
    if jogador != computador:
        print('Errado, tente novamente!')
        tentativas += 1
    if jogador == computador:
        print('Parabéns! Você acertou!')
print('O número de tentativas foi {}' .format(tentativas))