try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Valor inválido!')
except ZeroDivisionError:
    print('Não foi possível dividir por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar o valor!')
except Exception as erro:
    print(f'Ocorreu um erro: {erro.__cause__}')
else:
    print(f'O resultado foi {r}')
finally:
    print('Volte sempre! Muito obrigado!')
