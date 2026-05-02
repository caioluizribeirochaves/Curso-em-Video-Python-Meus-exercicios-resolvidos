# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        pos = 0 # Depois que o primeiro número for lido, a posição jamais voltará a ser 0, então esse comando abaixo vai ser lido até o final
        while pos < len(lista): # Len(lista) vai ler a quantidade de elementos presentes na lista
            if valor <= lista[pos]: # lista[pos] vai pegar o valor que veio depois do primeiro valor e vai comparar ele com o primeiro e assim por diante
                lista.insert(pos, valor) # Esse comando vai definir a posição em que o número vai entrar na lista
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')