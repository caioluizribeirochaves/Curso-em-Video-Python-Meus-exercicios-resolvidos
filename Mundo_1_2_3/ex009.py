n = int(input('Digite um número para ver a tabuada: '))
print(f'Tabuada de {n}: ')
for i in range(1, 100):
    print(f'{n} x {i} = {n * i}')

# tabela no formato original sem utilização de outras ferramentas:
#
#print('{} x {:2} = {}' .format(n, 1, n*1))
#print('{} x {:2} = {}' .format(n, 2, n*2))
#print('{} x {:2} = {}' .format(n, 3, n*3))
#print('{} x {:2} = {}' .format(n, 4, n*4))
#print('{} x {:2} = {}' .format(n, 5, n*5))
#print('{} x {:2} = {}' .format(n, 6, n*6))
#print('{} x {:2} = {}' .format(n, 7, n*7))
#print('{} x {:2} = {}' .format(n, 8, n*8))
#print('{} x {:2} = {}' .format(n, 9, n*9))
#print('{} x {:2} = {}' .format(n, 10, n*10))
