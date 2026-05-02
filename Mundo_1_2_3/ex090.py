# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['Nome'] = str(input('Nome do aluno: ')).strip().capitalize()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 >= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-=' * 20)
for c in aluno:
    print(f' - {c} é igual a {aluno[c]}')
