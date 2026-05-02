# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
jogos = []
todososjogos = []
print('-='*30)
print(f"{' JOGO NA MEGA SENA ':=^60}")
print('-='*30)
quantidade = int(input('Quantos jogos deseja gerar: '))
print('GERANDO...')
sleep(1)
for c in range(0, quantidade):
    contador = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in jogos:
            jogos.append(numeros)
            contador += 1
        if contador >= 6:
            break
    jogos.sort()
    todososjogos.append(jogos[:])
    jogos.clear()
for i, jogo in enumerate(todososjogos):
    print(f'Jogo {i+1}: {jogo}')
    sleep(1)
print('-='*30)
print(f"{' BOA SORTE! ':=^60}")
print('-='*30)
