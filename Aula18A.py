galera = []
dados = []
totmaior = totmenor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    print(f'{p[0]} tem {p[1]} anos', end=', ')
    if p[1] >= 21:
        print('é maior de idade')
        totmaior += 1
    else:
        print('é menor de idade')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade')
