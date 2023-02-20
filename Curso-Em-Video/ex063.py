print(f'{" EXERCÍCIO 63 ":=^40}')

# Exercício Python 63: Escreva um programa que leia um número N
# inteiro qualquer e mostre na tela os N primeiros elementos de
# uma Sequência de Fibonacci. Exemplo:
#
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)

termos = int(input('Quantos termos você quer mostrar? ').strip())
termoanterior = 0
termo = 0

print('~' * 20)
for i in range(0, termos - 1):
    if i == 1:
        termo = 1
        print(f'{termo}', end=' \u21E2 ')
    termo += termoanterior
    print(f'{termo}', end=' \u21E2 ')
    termoanterior = termo - termoanterior
print('FIM')
print('~' * 20)
