# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "Santo".
cidade = str(input('Digite o nome da cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
