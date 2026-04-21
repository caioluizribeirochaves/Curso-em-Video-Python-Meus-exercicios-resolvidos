# Faça o um programa que leia uma frase pelo teclado e mostre
# Quantas vezes aparece a letra "A"
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.' .format(frase.count('A')))
# Em que posição ela aparece a primeira vez
print('A primeira letra A apareceu na posição {}.' .format(frase.find('A') + 1))
print('A última letra A apareceu na posição {}.' .format(frase.rfind('A') + 1))

