from ex115lib.ex115mod import cabeçalho


def arqExiste(nome):
    try:
        a= open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'\033[32mArquivo {nome} criado com sucesso!\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mERRO ao ler o Arquivo!\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
