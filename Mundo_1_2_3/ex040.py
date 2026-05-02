# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#  - Média abaixo de 5.0: REPROVADO
#  - Média entre 5.0 e 6.9: RECUPERAÇÃO
#  - Média 7.0 ou superior: APROVADO
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A sua primeira nota foi {} e a segunda nota foi {}, a sua média é {}.' .format(n1, n2, media))
if media >= 7:
    print('Parabéns! Você foi APROVADO!')
elif 6.9 >= media >= 5:
    print('Você está de RECUPERAÇÃO...')
elif media < 5:
    print('Você foi REPROVADO!')
