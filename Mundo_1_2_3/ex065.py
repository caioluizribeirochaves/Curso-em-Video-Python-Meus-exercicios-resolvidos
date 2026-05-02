# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
n = 0
soma = 0
cont = 0
maior = 0
menor = 0
continuar = 'S'
while continuar in 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
print('A média entre os {} números digitados foi {:.2f}' .format(cont, soma/cont))
print('O maior número digitado foi {} e o menor foi {}' .format(maior, menor))
