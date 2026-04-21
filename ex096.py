# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno.
def area(l, c):
    a = l * c
    print(f'A área do terreno com largura de {l}m e comprimento de {c}m é igual a {a}m2.')


print(f'{"CONTROLE DE TERRENO":^30}')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)