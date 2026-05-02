# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesas
# C) Uma listagem com as pessoas mais leves
pessoas = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')).strip().capitalize())
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
print(f'A quantidade de pessoas cadastradas foi {len(pessoas)}')
print(f'O maior peso registrado foi {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso registrado foi {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
