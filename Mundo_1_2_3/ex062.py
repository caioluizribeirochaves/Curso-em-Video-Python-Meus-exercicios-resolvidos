# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 0 programa encerrará quando ele disser que quer mostrar 0 termos.
print('-=' * 10)
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
termo = primeiro
contador = 1
perg = 10
total = 0
while perg != 0:
    total = total + perg
    while contador <= total:
        print('{} -> ' .format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    perg = int(input('Deseja mostrar mais quantos termos? '))
print('Progressão finalizada com {} termos mostrados' .format(total))
