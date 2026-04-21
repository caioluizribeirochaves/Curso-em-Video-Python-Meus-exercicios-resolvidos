# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
cont = 0
n = int(input('Digite um número inteiro: '))
for c in range(1, n + 1):
    if n % c == 0 and n % n == 0:
        print('\033[1;33m', end=' ')
        print(f'{c}', end=' ')
        cont += 1
    else:
        print('\033[1;34m', end=' ')
        print(f'{c}', end=' ')
print('\n\033[mO número {} foi divisível {} vezes' .format(n, cont))
if cont == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')
