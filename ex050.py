# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o
s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c} número: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'A soma entre todos os {cont} números pares digitados é {s}')
