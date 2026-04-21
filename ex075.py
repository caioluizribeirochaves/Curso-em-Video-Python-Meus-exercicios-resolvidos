# Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em um tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
numpar = 0
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último valor: ')))
print(f'Você digitou os valores: {num}')

print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O valor 3 pareceu na {num.index(3) + 1} posição' if 3 in num else 'O valor 3 não está presente na lista')
print(f'Os valores pares digitados foram', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
