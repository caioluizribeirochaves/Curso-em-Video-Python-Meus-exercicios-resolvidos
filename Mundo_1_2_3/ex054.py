# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    idade = int(input('Em que ano a {} pessoa nasceu? ' .format(c)))
    idadeatual = ano - idade
    if idadeatual >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Tivemos ao todo {} pessoas maiores de idade' .format(totmaior))
print('E também tivemos {} pessoas menores de idade' .format(totmenor))
