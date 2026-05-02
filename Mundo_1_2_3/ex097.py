# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# ex: escreva('Olá, Mundo!')
# saída: -------------
#         Olá, mundo!
#        -------------

def texto(txt):
    print('~' * len(txt))
    print(txt)
    print('~' * len(txt))


txt = str(input('Digite uma frase para ver uma mágica: '))
texto(txt)
