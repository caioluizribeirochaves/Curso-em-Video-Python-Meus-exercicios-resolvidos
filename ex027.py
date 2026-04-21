# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
nome = str(input('Digite seu nome completo: '))
# Primeiro nome
primeiro_ultimo_nome = nome.split()
print(primeiro_ultimo_nome[0])
# Último nome
print(primeiro_ultimo_nome[-1])
