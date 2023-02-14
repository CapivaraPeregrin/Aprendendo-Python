import random

# Anotações da aula 10

# nome = str(input('Qual é o seu nome? '))
# if nome == 'Gustavo':
#     print('Que nome lindo você tem!')
# print('Bom dia, {}'.format(nome))
#
# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a primeira nota: '))
# n = (n1 + n2) / 2
# print('Parabéns' if n >= 6 else 'Estude mais')

print('====== EXERCÍCIO 28 ======')
#Exercício Python 28: Escreva um programa que faça o computador
# “pensar” em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[1m"
REVERSE = "\033[;7m"
YELLOW = "\033[1;33m"
PURPLE = "\033[0;35m"

print(YELLOW + '-=-' * 20)
print(BLUE + 'Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(YELLOW + '-=-' * 20)
numeroPensado = random.randint(0, 5)

palpite = int(str(input(RESET + 'Em que número eu pensei? ')).strip())
print(PURPLE + 'PROCESSANDO...')
if palpite == numeroPensado:
    print(GREEN + 'PARABÉNS! Você conseguiu me vencer!')
else:
    print(RED + 'GANHEI! Eu pensei no número {} e não no {}!'.format(numeroPensado, palpite))
