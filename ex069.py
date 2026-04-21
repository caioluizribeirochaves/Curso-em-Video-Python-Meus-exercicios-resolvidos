# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos.
pessoas18 = homem = mulher20 = 0
while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' * 30)
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
    if idade >= 18:
        pessoas18 += 1
    if sexo in 'Mm':
        homem += 1
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {pessoas18}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher20} mulheres com menos de 20 anos.')
