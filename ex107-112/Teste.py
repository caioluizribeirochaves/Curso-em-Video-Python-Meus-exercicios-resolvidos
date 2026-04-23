from moeda import aumentar, diminuir, dobro, metade, form
num = float(input('Digite um número: R$'))
print(f'O dobro de {form(num)} é {form(dobro(num))}')
print(f'A metade de {form(num)} é {form(metade(num))}')
print(f'Aumentado 10% de {form(num)} é {form(aumentar(num, 10))}')
print(f'Diminuindo 10% de {form(num)} é {form(diminuir(num, 10))}')
 