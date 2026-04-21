# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até um valor correto.
sexo = ['M', 'F']
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo: [M/F]: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Digite novamente...')
if sexo == 'F':
    print('Sexo FEMININO registrado com sucesso!')
else:
    print('Sexo MASCULINO registrado com sucesso!')

