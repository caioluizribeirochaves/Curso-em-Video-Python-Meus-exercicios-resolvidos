def texto(txt):
    print('-' * 60)
    print(txt)
    print('-' * 60)
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} e {b} = {s}')
def contador(*num):
    print(num)
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} valores')
    for valor in num:
        print(f'{valor} ', end='')



# Programa principal
texto(f'{"EU VOU SER O MELHOR PROGRAMADOR QUE ESSE MUNDO JÁ VIU":^60}')
soma(5, 10)
soma(4, 9)
soma(b=8, a=10)
contador(2, 4, 3, 5, 6, 7)