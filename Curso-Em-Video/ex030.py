print('====== EXERCÍCIO 30 ======')

# Exercício Python 30: Crie um programa que leia um número
# inteiro e mostre na tela se ele é PAR ou ÍMPAR.

PURPLE = "\033[0;35m"
BLUE = "\033[1;34m"
RESET = "\033[0;0m"

numero = int(input(PURPLE + 'Me diga um número qualquer: ' + RESET))

print('O número {} é '.format(numero) + BLUE, end = '')
print('PAR' if numero % 2 == 0 else 'ÍMPAR')
