import time
import random

print('{:=^40}'.format(' EXERCÍCIO 45 '))

# Exercício Python 45: Crie um programa que
# faça o computador jogar Jokenpô com você.

print('Suas opções: ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

opcaoPlayer = int(input('Qual é a sua jogada? '))
if opcaoPlayer != 0 or opcaoPlayer != 1 or opcaoPlayer != 2:
    opcaoPlayer = (opcaoPlayer**2) / opcaoPlayer
    opcaoPlayer = int((opcaoPlayer // 3) + (opcaoPlayer % 3) - 1)
    print(f'Sua opção é inválida por isso foi readequada para {opcaoPlayer}')

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')

opcoes = [[0, 'Pedra'], [1, 'Papel'], [2, 'Tesoura']]
escolhaComputador = random.randint(0, 2)

print('-=' * 15, end='-\n')
print('Computador jogou {}'.format(opcoes[escolhaComputador][1]))
print('Jogador jogou {}'.format(opcoes[opcaoPlayer][1]))
print('-=' * 15, end='-\n')

if escolhaComputador == opcaoPlayer:
    print('EMPATE')
elif opcoes[escolhaComputador - 1] == opcoes[opcaoPlayer]:
    print('COMPUTADOR VENCE')
elif opcoes[opcaoPlayer - 1] == opcoes[escolhaComputador]:
    print('JOGADOR VENCE')
