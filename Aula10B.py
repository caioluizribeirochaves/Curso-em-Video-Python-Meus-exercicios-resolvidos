nome = str(input('Digite seu nome: ')).strip().capitalize()
if nome == 'Caio':
    print('Que nome maravilhoso você tem!')
else:
    print('Seu nome é tão normal...')
print('Bom dia, {}!' .format(nome))
