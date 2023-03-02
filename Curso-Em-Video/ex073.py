print(f'{" EXERCÍCIO 73 ":=^50}')

# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
        'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza',
        'São Paulo', 'América-MG', 'Botafogo', 'Santos',
        'Goiás', 'Red Bull Bragantino', 'Coritiba', 'Cuiabá',
        'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

print('-=' * 50)
print(f'Lista de times do brasileirão: {times}')
print('-=' * 50)
print(f'Os 5 primeiros são {times[:5]}')
print('-=' * 50)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 50)

posicao = times.index('Corinthians')
print(f'O Corinthians está na {posicao}ª posição')
