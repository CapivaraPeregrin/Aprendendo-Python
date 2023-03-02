import time
from random import randint
print(f'{" EXERCÍCIO 88 ":=^50}')

# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA
# a criar palpites.O programa vai perguntar quantos jogos serão gerados e
# vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em
# uma lista composta.

print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)

numJogos = int(input('Quantos jogos você quer que eu sorteie? '))
lista = [[] for i in range(0, numJogos)]
print('-=' * 5, ' SORTEANDO {} JOGOS '.format(numJogos), '-=' * 5)

for i in range(0, numJogos):
    while len(lista[i]) != 6:
        num = randint(1, 60)
        if num not in lista[i]:
            lista[i].append(num)
        lista[i].sort()
    time.sleep(0.5)
    print(f'Jogo {i+1}: {lista[i]}')

print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)
