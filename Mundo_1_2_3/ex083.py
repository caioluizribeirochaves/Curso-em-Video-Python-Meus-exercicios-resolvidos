# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expr = str(input('Digite sua expressão: '))
pilha = [] # vai servir para armazenar uma informação que vai ser usada de paramêtro de comparação, nesse caso será '(' e ')'.
for simb in expr: # vai verificar se os '(' e ')', estão presentes na expressão
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0: # vai ler o comprimento da string e vai excluir o último '(' que foi digitado, a fim de alcançar o 0
            pilha.pop()
        else:
            pilha.append(')') # caso não tenha um par para o ')', ele é adicionado a pilha
            break
if len(pilha) == 0:
    print('A sua expressão é valida!')
else:
    print('A sua expressão é inválida!')
