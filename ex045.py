# Crie um programa que faça o computador jogar Jokenpô com voçê.
import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.choice(itens)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=-' * 21)
if jogador == 1 and computador == 'Pedra':
    print('Você escolheu PAPEL e EU escolhi PEDRA. Parabéns, você ganhou!')
elif jogador == 0 and computador == 'Tesoura':
    print('Você escolheu PEDRA e EU escolhi TESOURA. Parabéns, você ganhou!')
elif jogador == 2 and computador == 'Papel':
    print('Você escolheu TESOURA e EU escolhi PAPEL. Parabéns, você ganhou!')
elif jogador == 0 and computador == 'Papel':
    print('Você escolheu PEDRA e EU escolhi PAPEL. Eu ganhei! Tente novamente.')
elif jogador == 2 and computador == 'Pedra':
    print('Você escolheu TESOURA e EU escolhi PEDRA. Eu ganhei! Tente novamente.')
elif jogador == 1 and computador == 'Tesoura':
    print('Você escolheu PAPEL e EU escolhi TESOURA. Eu ganhei! Tente novamente.')
elif jogador == 0 and computador == 'Pedra':
    print('Você escolheu PEDRA e EU escolhi PEDRA. Empatamos...')
elif jogador == 1 and computador == 'Papel':
    print('Você escolheu PAPEL e EU escolhi PAPEL. Empatamos...')
elif jogador == 2 and computador == 'Tesoura':
    print('Você escolheU TESOURA e eu escolhi TESOURA. Empatamos...')
else:
    print('{:=^63}'.format(' Jogada invalida! '))
print('-=-' * 21)
