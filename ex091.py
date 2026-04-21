# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
jogadores = {}
print('Valores sorteados:')
sleep(0.5)
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)
    print(f'[Jogador {c}] tirou {jogadores[f'jogador{c}']} no dado.')
    sleep(0.5)
from operator import itemgetter
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-=' * 40)
print('== Ranking dos jogadores ==')
for k, v in enumerate(ranking):
    print(f'{k + 1}o. lugar: [{v[0]}] com {v[1]}.')
    sleep(0.5)
