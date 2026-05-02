# TUPLAS SÃ0 IMUTÁVEIS
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-3])
print(lanche[0])
print(lanche[:2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[-2:])
print(lanche[-3:])

print(sorted(lanche)) # coloca em ordem alfabética

for comida in lanche:
    print(f'Comi {comida}')

for cont in range(0, len(lanche)):
    print(f'Comi {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Comi {comida} na posição {pos}')

print('Comi pra caramba')