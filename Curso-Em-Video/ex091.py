from time import sleep
from random import randint
from operator import itemgetter

print(f'{" EXERCÍCIO 91 ":=^50}')

# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham
# resultados aleatórios. Guarde esses resultados em um dicionário em Python. No
# final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
# número no dado.

ranking = list()
sorteio = {'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)}

print('Valores sorteados: ')
for k, v in sorteio.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)

print('-=' * 20)
print('   == RANKING DOS JOGADORES ==')
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
