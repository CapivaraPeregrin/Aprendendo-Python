import random

print('{:=^40}'.format(' EXERCÍCIO 58 '))

# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o
# computador vai “pensar” em um número entre 0 e 10. Só que
# agora o jogador vai tentar adivinhar até acertar, mostrando
# no final quantos palpites foram necessários para vencer.

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
num = random.randint(0, 10)
palpite = -1
tentativas = 0

print(num)
while num != palpite:
    palpite = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if num == palpite:
        print(f'Acertou com {tentativas} tentativas. Parabéns!')
    elif num < palpite:
        print('Menos... Tente mais uma vez.')
    elif num > palpite:
        print('Mais... Tente mais uma vez.')
