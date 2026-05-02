# Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
n  = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        s += c
        n = n + 1
print(f'O somatório de todos os {n} números impares divisiveis por 3 é {s}')
