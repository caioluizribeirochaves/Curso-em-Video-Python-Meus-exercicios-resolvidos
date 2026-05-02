nome = str(input('Digite seu nome: ')).strip().capitalize()
if nome == 'Caio':
    print('Que nome lindo!')
elif nome == 'Paulo' or nome == 'Ana' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Amanda Arthur Ryan Clayton Camila Giovanna Vitória':
    print('Seu nome é bem normal.')
else:
    print('Mamãe judiou.')
print('Tenha um bom dia!')
