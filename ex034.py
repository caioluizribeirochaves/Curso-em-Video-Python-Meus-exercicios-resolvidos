# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250.00, calcule um aumento de 10%.
# Para inferiores ou iguais, o aumento é de 15%
from time import sleep
salario = float(input('Digite seu salário para que seja calculado o aumento, R$: '))
print('PROCESSANDO...')
sleep(2)
if salario <= 1250:
    print('Seu novo salário é de R${:.2f}' .format((salario + (salario * 0.15))))
else:
    print('Seu novo salário é de {:.2f}' .format((salario + (salario * 0.10))))
