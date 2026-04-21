# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.
distancia = float(input('Digite a distância a ser percorrida na viagem: '))
if distancia <= 200:
    print('Você deverá pagar um total de R${:.2f}.' .format((distancia * 0.50)))
else:
    print('Você deverá pagar um total de R${:.2f}.' .format((distancia * 0.45)))
print('-' * 40)
print('         TENHA UMA BOA VIAGEM!')
print('-' * 40)
