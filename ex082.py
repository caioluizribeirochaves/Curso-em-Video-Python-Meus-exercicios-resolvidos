# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
par = []
impar = []
while True:
    n = (int(input('Digite um valor: ')))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    if n % 2 == 1:
        impar.append(n)
    opcao = ' '
    while opcao  not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao in 'N':
        break
lista.sort()
par.sort()
impar.sort()
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')


# for i, v in enumerate(lista):
#     if v % 2 ==0:
#         par.append(v)
#     elif v % 2 == 1:
#         impar.append(v)
