# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Quanto você quer sacar? R$'))
total = valor # igualar o total ao valor para que se possa iniciar a contagem de cédulas
cedula = 50 # Deve informar o valor da cédula mais alta
totaldecedula = 0 # registrar o total de cédulas para cada valor
while True:
    if total >= cedula: # Enquanto o valor total for maior que o valor da cedula, ele vai ficar a retirar o valor da cedula até que zere
        total -= cedula # Esse comando serve para tirar o valor da cédula até não dar mais.
        totaldecedula += 1 # Aqui ele adiciona o total de cedulas utilizadas até não ser possível mais retirar
    else: # Nesse else, é aonde acontece a filtragem de quais cédulas serão mostradas e utilizadas
        if totaldecedula > 0: # enquanto o valor for diferente de 0 ele vai continuar a retirar cédulas
            print(f'Total de {totaldecedula} cédulas de R${cedula}') # Serve para mostrar a quantidade de cédulas utilizadas para o valor digitado
        if cedula == 50: # Caso não dê mais para retirar cédulas de 50, ele irá começar a retirar cédulas de 20
            cedula = 20
        elif cedula == 20: # Caso não dê mais para retirar cédulas de 20, ele irá começar a retirar cédulas de 10
            cedula = 10
        elif cedula == 10: # Caso não dê mais para retirar cédulas de 10, ele irá começar a retirar cédulas de 1
            cedula = 1
        totaldecedula = 0 # Zera a contagem para cada novo valor de cédula que irá assumir a seguir
        if total == 0: # Pausa o programa quando o valor chegar a 0
            break
