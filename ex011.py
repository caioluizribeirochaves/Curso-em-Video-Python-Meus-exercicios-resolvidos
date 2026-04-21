import math
larg = float(input('Qual a largura da parede: '))
alt = float(input('Qual a altura da parade: '))
area = larg * alt
tinta = math.ceil(area / 2)
print('A área da parade é {}m²' .format(area), end=' ')
print(', para isso será necessário {:.2f} litro(s) de tinta.' .format(tinta))
