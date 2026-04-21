valor = int(input('Digite um valor em metros: '))
km =  valor / 1000
hm = valor / 100
dam = valor / 10
dm = valor * 10
cm = valor * 100
mm = valor * 1000
print('{}m é equivale a {}km, {}hm, {}dam, {:.0f}dm, {:.0f}cm, e {:.0f}mm.' .format(valor, km, hm, dam, dm, cm, mm))
