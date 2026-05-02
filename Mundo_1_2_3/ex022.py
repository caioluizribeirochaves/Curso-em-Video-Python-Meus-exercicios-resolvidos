# Primeira parte, leia o nome
nome = str(input('Digite seu nome completo: ')).strip()
# Nome com todas as letras maiúsculas
print('Seu nome em maiúsculo é {}' .format(nome.upper()))
# Nome com todas as letras minúsculas
print('Seu nome em minúsculo é {}' .format(nome.lower()))
# Quantas letras ao todo sem considerar os espaços
print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' ')))
# Quantas letras tem o primeiro nome
nome1 = nome.split()
print('Seu primeiro nome é {}, e ele tem {} letras' .format(nome1[0], len(nome1[0])))
