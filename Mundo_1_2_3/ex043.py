# Desenvolva uma lógica que leia o peso a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#  - Abaixo de 18.5: Abaixo do peso
#  - Entre 18.5 e 25: Peso ideal
#  - 25 até 30: Sobrepeso
#  - 30 até 40: Obesidade
#  - Acima de 40: Obesidade mórbida
from time import sleep
print('-' * 20)
print('CALCULADORA IMC')
print('-' * 20)
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
print('PROCESSANDO...')
sleep(2)
print('Seu IMC é {:.2f}' .format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc >= 25 and imc <= 30:
    print('Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')
