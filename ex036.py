# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep
valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Quantos anos de financiamento? '))
print('CALCULANDO...')
sleep(2)
financiamento = valor / (anos * 12)
if financiamento > salario * 30 / 100:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}. \nSeu financiamento foi \033[4;31mnegado!\033[4;31m' .format(valor, anos, financiamento))
elif financiamento < salario * 30 / 100:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}. \nSeu financiamento foi \033[4;32maprovado!\033[4;32m' .format(valor, anos, financiamento))
