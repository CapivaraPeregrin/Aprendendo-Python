import math

print(f'{" EXERCÍCIO 60 ":=^40}')

# Exercício Python 060: Faça um programa que leia um
# número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

num1 = int(input('Digite um número para \ncalcular seu Fatorial: '))

fatorial = math.factorial(num1)
expressao = ''
for i in range(num1, 0, -1):
    expressao += str(i)
    if i != 1:
        expressao += ' x '

print(f'Calculando {num1}! = ' + expressao + f' = {fatorial}')
