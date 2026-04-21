# Crie um programa onde o usuário possa digitar ste valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final mostre os valores pares e ímpares em ordem crescente.
valores = [[], []]
valor = 0
for c in range(1, 8):
    valor = (int(input(f'Digite o {c}o. valor: ')))
    if valor % 2 == 0 and valor != 0:
        valores[0].append(valor)
    else:
        if valor % 2 == 1:
            valores[1].append(valor)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares foram {valores[0]}')
print(f'Os valores impares foram {valores[1]}')
