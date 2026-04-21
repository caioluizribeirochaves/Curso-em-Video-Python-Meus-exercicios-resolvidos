# Crie um programa que leia uma matriz de dimensão 3x3 e a preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
print('-=' * 40)
for c in matriz:
    for i,v in enumerate(c, 1):
        print(f'[{v:^5}]', end=' ')
        if i % 3 == 0: # A cada 3 valores lidos, um print será realizado para quebrar a linha
            print()
