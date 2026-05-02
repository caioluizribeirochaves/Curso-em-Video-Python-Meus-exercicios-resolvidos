# Crie um programa que leia nome de duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente
alunos = []
temp = []
while True:
    temp.append(str(input('Nome do aluno: ')).strip().capitalize())
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    alunos.append(temp[:])
    temp.clear()
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-'*32)
print(f"{'No.':<4} {'NOME':<5} {'MÉDIA':>20}")
print('-'*32)
for i, a in enumerate(alunos):
    print(f'{i:<4} {a[0]:.<20} {((a[1] + a[2])/ 2):>4}')
print('-'*32)
while opcao != 999:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao <= len(alunos) - 1:
        print(f'Notas de {alunos[opcao][0]} são [{alunos[opcao][1]}] e [{alunos[opcao][2]}]')
    if opcao == 999:
        print('FIM DO PROGRAMA')
        break
