# Refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 1000):
    print(f'{n} x {i} = {n * i}')
