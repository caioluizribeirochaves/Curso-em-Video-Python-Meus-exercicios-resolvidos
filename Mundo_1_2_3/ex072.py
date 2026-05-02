# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número teclado(entre 0 e 20) e mostrá-lo por extenso
extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente...', end='')
print(f'O número digitado foi {extenso[num]}') # esse comando serve para linkar o número digitado no input com a tupla referente no banco de dados.
while True:
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'Ss':
            num = int(input('Digite um número entre 0 e 20: '))
            print(f'O número digitado foi {extenso[num]}')
    if opcao in 'Nn':
        break
print('FIM DO PROGRAMA')