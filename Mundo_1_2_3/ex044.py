# Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
#  - Á vista dinheiro/cheque: 10% de desconto
#  - Á vista no cartão: 5% de desconto
#  - Em até 2x no cartão: preço normal
#  - 3x ou mais no cartão: 20% de juros
print('{:=^40}' .format(' LOJAS CAMALEÃO '))
valor = float(input('Informe o valor da sua compra, R$: '))
formapag = int(input('''SELECIONE A FORMA DE PAGAMENTO:
[ 1 ] Á vista em dinheiro/cheque
[ 2 ] Á vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] Em 3x ou mais no cartão
SELECIONE A OPÇÃO: '''))
if formapag == 1:
    print('O valor de R${} com os descontos aplicados para pagamento á vista no dinheiro/cheque, é de R${:.2f}.' .format(valor, valor - (valor * 0.10)))
elif formapag == 2:
    print('O valor de R${} com os descontos aplicados para pagamento á vista no cartão, é de R${:.2f}.' .format(valor, valor - (valor * 0.05)))
elif formapag == 3:
    print('O valor a ser pago é de R${:.2f}, podendo ser dividido em até duas parcelas de {:.2f} SEM JUROS.' .format(valor, valor / 2))
elif formapag == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('O valor a ser pago é de R${}, ou em {}x de R${} COM JUROS.' .format(valor + (valor * 0.20), parcelas, (valor + (valor * 0.20)) / parcelas ))
else:
    print('OPÇÃO INEXISTENTE, TENTE NOVAMENTE...')
