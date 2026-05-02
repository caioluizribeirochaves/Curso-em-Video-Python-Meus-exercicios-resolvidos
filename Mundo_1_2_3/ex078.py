# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valor = []
# maior = menor = 0
for num in range(0, 5):
    valor.append(int(input(f'Digite um valor para posição {num}: ')))
    # if num == 0:
    #     maior = menor = valor[num]
    # else:
    #     if valor[num] > maior:
    #         maior = valor[num]
    #     if valor[num] < menor:
    #         menor = valor[num]
print(f'O maior digitado foi {max(valor)} e se encontra na posição', end=' ')
for i, v in enumerate(valor):
    if v == max(valor):
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {min(valor)} e se encontra na posição', end=' ')
for i, v in enumerate(valor):
    if v == min(valor):
        print(f'{i}...', end='')
