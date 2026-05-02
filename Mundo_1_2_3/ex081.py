# Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'A quantidade de valores digitados foi {len(lista)}')
lista.sort(reverse=True)
print(f'A lista ordenada em ordem decrescente {lista}')
print(f'O valor 5 está na lista, na posição ' if 5 in lista else 'O valor 5 não está presente na lista', end='')
for i, v in enumerate(lista):
    if v == 5:
        print(f'{i}...', end='')
