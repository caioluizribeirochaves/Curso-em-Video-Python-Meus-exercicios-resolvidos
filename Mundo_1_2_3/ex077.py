# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in palavras:
    print(f'\nNa palavra \033[35m{palavra.upper()}\033[m temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'\033[34m{letra}\033[m', end=' ')
