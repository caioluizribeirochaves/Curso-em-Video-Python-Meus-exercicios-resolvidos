# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    print('-' * 35)
    for m in range(1, 11):
        print(f'{valor} x {m} = {valor * m}')
    print('-' * 35)
print('PROGRAMA DE TABUADA ENCERRADO...Volte sempre!')
