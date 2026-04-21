import math
angulo = float(input('Digite um angulo qualquer: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Para o angulo {} informado, o valor de seu seno é {:.3f}, seu cosseno é {:.3f}, e a sua tangente é {:.3f}.' .format(angulo, seno, cosseno, tangente))
