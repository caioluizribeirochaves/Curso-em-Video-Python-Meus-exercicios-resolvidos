n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digte a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}.' .format(m))
if m >= 6:
    print('Média boa!')
else:
    print('Média ruim...')
