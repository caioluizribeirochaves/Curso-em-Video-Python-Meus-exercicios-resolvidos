# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))
if n1 > n2 and n1 >= n3:
    print('O maior número é {}' .format(n1))
if n3 > n1 and n3 > n2:
    print('O maior número é {}' .format(n3))
if n2 >= n3 and n2 > n1:
    print('O maior número é {}' .format(n2))
else:
    if n1 < n2 and n1 <= n3:
        print('O menor número é {}' .format(n1))
    if n2 <= n3 and n2 < n1:
        print('O menor número é {}' .format(n2))
    if n3 < n1 and n3 < n2:
        print('O menor número é {}' .format(n3))
if n1 == n2 == n3:
    print('Todos o números tem o mesmo valor')


# Verificando quem é o menor
# menor = a
# if b < a and b < c:
#   menor = b
# if c < a and c < b:
#   menor = c
# Verificando quem é o maior
# maior = a
# if b > a and b > c:
#   maior = b
# if c > a and c > b:
#   maior = c
# print('O menor valor digitado foi {}' .format(menor))
# print('O maior valor digitado foi {}' .format(maior))
