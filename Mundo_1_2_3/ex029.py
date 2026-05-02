# Escreva um programa que leia a velocidade de um carro,
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limite.
from time import sleep
print('-=-' * 13)
print('POSTO DE FISCALIZAÇÃO AVANÇADO DO DETRAN')
print('-=-' * 13)
velocidade = float(input('Informe a velocidade do carro: '))
print('PROCESSANDO...')
sleep(2)
if velocidade > 80:
    print('Multado! Velocidade de {} exede o limite de 80Km!' .format(velocidade))
    print('A multa será de {:.2f}.' .format((velocidade - 80) * 7))
else:
    print('Velocidade permitida!')
sleep(2)
print('-=-' * 13)
print('         Tenha um bom dia!')
print('-=-' * 13)
