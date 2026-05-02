# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while
print('-=' * 10)
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Informe a razão: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} -> ' .format(termo), end='')
    termo += razao
    contador += 1
print('FIM')
