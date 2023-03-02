print(f'{" EXERCÍCIO 99 ":=^50}')

# Exercício Python 099: Faça um programa que tenha uma função chamada
# maior(), que receba vários parâmetros com valores inteiros. Seu
# programa tem que analisar todos os valores e dizer qual deles é
# o maior.


def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    mais = 0
    if len(num) > 0:
        mais = num[0]
    for c in num:
        if c > mais:
            mais = c
        print(c, end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mais}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
