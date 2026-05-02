# Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número inteiro qualquer: '))
if num % 2 == 0:
    print('O número {} é PAR' .format(num))
else:
    print('O número {} é IMPAR' .format(num))
