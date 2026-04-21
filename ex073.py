# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.
colocacao = ('Palmeiras', 'São Paulo', 'Fluminense', 'Bahia',
             'Athletico Paranaense', 'Coritiba', 'Flamengo', 'Botafogo',
             'Vasco da Gama', 'Atlético-MG', 'Grêmio', 'Red Bull Bragantino',
             'Vitória', 'Santos', 'Corinthians', 'Internacional', 'Chapecoense',
             'Cruzeiro', 'Mirassol', 'Remo-PA')
print('-=-' * 30)
print(f'Os 5 primeiros colocados são {colocacao[:5]}')
print('-=-' * 30)
print(f'Os últimos 4 colocados da tabela são {colocacao[-4:]}')
print('-=-' * 30)
print(f'Lista dos times em ordem alfabética {sorted(colocacao)}')
print('-=-' * 30)
print(f'A Chapecoense está na {colocacao.index('Chapecoense') + 1} posição')
print('-=-' * 30)
