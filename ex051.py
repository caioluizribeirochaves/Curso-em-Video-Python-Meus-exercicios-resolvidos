# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('=' * 32)
print('OS 10 PRIMEIROS TERMOS DE UMA PA')
print('=' * 32)
n = int(input('Primeiro termo: '))
razao = int(input('Qual a razão: '))
decimo = razao + (10 - 1) * razao
for c in range(n, decimo + razao, razao):
    print(c, end=' ')
print('FIM')
