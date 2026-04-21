# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite uma frase/palavra: ')).strip().upper()
palavras = frase.split() #Serve para separar as palavras das frases em grupos
junto = ''.join(palavras) #Serve para juntar os grupos de palavras. No caso do uso de '' sem nada dentro, ele junta as palavras sem espaço
inverso = junto[::-1] #Serve para inverter a ordem do texto
#inverso = ''
#for letra in range(len(junto) -1, -1, -1):
#    inverso += junto[letra]
print('A frase/palavra {} invertida é {}' .format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não é um palíndromo')
