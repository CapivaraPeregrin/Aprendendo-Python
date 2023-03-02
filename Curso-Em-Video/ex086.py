print(f'{" EXERCÍCIO 86 ":=^50}')

# Exercício Python 086: Crie um programa que declare uma matriz de dimensão
# 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz
# na tela, com a formatação correta.

lista = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f'Digite um valor para [{i}, {j}]: '))
        lista[i].append(num)

print('-=' * 30)

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{lista[i][j]:^5}]', end='')
    print('')
