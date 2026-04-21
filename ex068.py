# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
contador = 0
while True:
    valor = int(input('Diga um valor entre 0 e 10: '))
    jogada = ' '
    while jogada not in 'PpIi':
        jogada = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    computador = randint(0, 10)
    print('-' * 30)
    if jogada == 'P':
        if (computador + valor) % 2 == 0:
            contador += 1
            print(f'Você jogou {valor} e o computador {computador}. O total de {computador + valor} deu PAR')
            print('-' * 30)
            print('Você VENCEU')
            print('Vamos jogar novamente...')
            print('-' * 30)
        if (computador + valor) % 2 == 1:
            print(f'Você jogou {valor} e o computador {computador}. O total de {computador +  valor} deu ÍMPAR')
            print('Você PERDEU!')
            print('-' * 30)
            break
    if jogada == 'I':
        if (computador + valor) % 2 == 0:
            print(f'Você jogou {valor} e o computador {computador}. O total de {computador + valor} deu PAR')
            print('-' * 30)
            print('Você PERDEU!')
            print('-' * 30)
            break
        if (computador + valor) % 2 == 1:
            contador += 1
            print(f'Você jogou {valor} e o computador {computador}. O total de {computador + valor} deu IMPAR')
            print('-' * 30)
            print('Você VENCEU')
            print('Vamos jogar novamente...')
            print('-' * 30)
print(f'GAME OVER! Você venceu {contador} vezes.')
