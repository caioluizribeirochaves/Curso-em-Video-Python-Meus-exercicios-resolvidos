# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
#  - O primeiro valor é maior
#  - O segundo valor é maior
#  - Não existe valor maior, os dois são iguais.

n1 = int(input('Digite o valor 1: '))
n2 = int(input('Digite o valor 2: '))
if n1 > n2:
    print('O \033[1;34mvalor 1\033[m é maior que o \033[1;31mvalor 2\033[m')
elif n1 < n2:
    print('O \033[1;34mvalor 2\033[m é maior que o \033[1;31mvalor 1\033[m')
else:
    print('Os valores são \033[1;32miguais\033[m')
