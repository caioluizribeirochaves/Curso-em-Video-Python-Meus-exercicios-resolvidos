# Junta as duas TUPLAS em uma só
# Nas tuplas podem haver dados de tipos difentes dentro dela
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c)) # Le quantos valores existem dentro da tupla
print(c.count(5)) # conta quantas vezes o valor se repete
print(c.index(8)) # mostra a posição do valor informado
 