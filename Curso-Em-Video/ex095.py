print(f'{" EXERCÍCIO 95 ":=^50}')

# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com
# vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.

time = []
jogador = dict()
while True:
    jogador['nome'] = input('Nome do Jogador: ').strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    for c in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())

    while True:
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break

print('-=' * 30)
print('cod', f'{"nome":<15}', f'{"gols":<15}', f'{"total":<5}' )
print('-' * 40)
for i, jog in enumerate(time):
    print(f'{i:>3}', f'{jog["nome"]:<15}', f'{str(jog["gols"]):<15}', f'{jog["total"]:<5}')

while True:
    print('-' * 40)
    num = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if num == 999:
        print('<< VOLTE SEMPRE >>')
        break
    elif num not in range(0, len(time)):
        print(f'ERRO! Não existe jogador com código {num}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[num]["nome"]}: ')
        for i, gol in enumerate(time[num]['gols']):
            print(f'    No jogo {i} fez {gol} gols.')
