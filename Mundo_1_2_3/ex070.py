# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.
print('-' * 30)
print('{:=^30}'.format(' LOJA CAMALEÃO '))
print('-' * 30)
soma = prod1000 = cont = prodb = 0
prodbarato = ''
while True:
    nomep = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    cont += 1
    soma += preco
    if preco >= 1000:
        prod1000 += 1
    if cont == 1 or preco < prodb:
        prodb = preco
        prodbarato = nomep
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-' * 30)
print(f'O total da compra foi R${soma:.2f}')
print(f'A quantidade de produtos que custaram mais de R$1000 reais foi {prod1000}')
print(f'O produto mais barato dessa lista foi \033[32m{prodbarato}\033[m que custou R${prodb:.2f}')
