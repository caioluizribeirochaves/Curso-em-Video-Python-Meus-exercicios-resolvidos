# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
# 1 para binário
# 2 para octal
# 3 para hexadecimal
n = int(input('Digite um número inteiro: '))
escolha = int(input('Escolha uma das bases para conversão: \n[ 1 ] converter para BINÁRIO \n[ 2 ] converter para OCTAL \n[ 3 ] converter para HEXADECIMAL \nSua opção: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}' .format(n, bin(n)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}' .format(n, oct(n)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}' .format(n, hex(n)[2:]))
else:
    print('Opção inválida, tente novamente.')
