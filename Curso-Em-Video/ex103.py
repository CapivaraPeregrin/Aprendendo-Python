print(f'{" EXERCÍCIO 103 ":=^50}')

# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols
# ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 30)
nom = input('Nome do Jogador: ').strip()
gol = str(input('Número de Gols: '))

if gol.isnumeric():
    gols = int(gol)
else:
    gols = ''
if nom.strip() == '' and gol.strip() == '':
    ficha()
elif nom.strip() == '':
    ficha(gols=gol)
elif gol.strip() == '':
    ficha(nome=nom)
else:
    ficha(nom, gol)
