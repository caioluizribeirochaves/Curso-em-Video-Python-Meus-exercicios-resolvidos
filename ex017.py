import  math
catop = float(input('Digite o cateto oposto: '))
catad = float(input('Digite o cateto adjacente: '))
hipotenusa = math.hypot(catop, catad)
print('Para um triangulo com cateto oposto {} e cateto adjacente {}, a hipotenusa vale {:.2f}' .format(catop, catad, hipotenusa))
