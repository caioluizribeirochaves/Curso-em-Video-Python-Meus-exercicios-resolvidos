# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
pessoas = {}
banco = []
totidade = 0
while True:
    pessoas['nome'] = str(input('Nome: ')).strip().capitalize()
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F')
    pessoas['sexo'] = sexo
    pessoas['idade'] = int(input('Idade: '))
    totidade += pessoas['idade']
    banco.append(pessoas.copy())
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N')
    if opcao == 'N':
        break
media =  totidade / len(banco)
print(f'A) Tivemos um total de {len(banco)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in banco:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print('\nD) Lista das pessoas que estão acima da média: ')
for p in banco:
    if p['idade'] >= media:
        print(f'    Nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]}. ')
print('<< ENCERRADO >>')
