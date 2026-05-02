pessoas = {'NOME': 'Caio', 'IDADE': 27, 'SEXO': 'M'}
pessoas['PESO'] = 96.2
for k, v in pessoas.items():
    print(f'{k} = {v}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
