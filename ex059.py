# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos números
# [ 5 ] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep
opcao = ['1', '2', '3', '4', '5']
print('-=-' * 10)
print('    PROJETO DE CALCULADORA')
print('-=-' * 10)
v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))
while opcao != 5:
    print('''LISTA DE OPERAÇÕES:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        print('Calculando...')
        sleep(1)
        print(f'A soma entre {v1} e {v2} é igual a {v1 + v2}')
    elif opcao == 2:
        print('Calculando...')
        sleep(1)
        print(f'A multiplicação entre {v1} e {v2} é igual a {v1 * v2}')
    elif opcao == 3:
        print('Calculando...')
        sleep(1)
        if v1 > v2:
            print(f'O valor {v1} é maior que o valor {v2}')
        elif v1 < v2:
            print(f'O valor {v2} é maior que o valor {v1}')
        elif v1 == v2:
            print(f'Os valores {v1} e {v2} são iguais')
    elif opcao == 4:
        print('Informe os valores novamente')
        v1 = float(input('Primeiro valor: '))
        v2 = float(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
        print('Obrigado por utilizar o programa!')
    else:
        print('Opção inválida. Tente novamente')
