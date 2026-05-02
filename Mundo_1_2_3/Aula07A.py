n1 = int(input("Digite um número: "))
n2 = int(input('Digte outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
sub = n1 - n2
p = n1 ** n2
di = n1 // n2
r = n1 % n2
print('A soma é {}, \n a multiplicação é {}, \n a divisisão é {:.3}, \n a subtração é {}' .format (s, m, d, sub), end=' ')
print(', \n a potência é {}, \n a divisão inteira é {}, \n e o resto é {}.' .format(p, di, r))