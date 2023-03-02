print(f'{" EXERCÍCIO 87 ":=^50}')

# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

lista = [[], [], []]
sumPares = 0
sumCol3 = 0

for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f'Digite um valor para [{i}, {j}]: '))
        lista[i].append(num)
        if num % 2 == 0:
            sumPares += num
        if j == 2:
            sumCol3 += num

print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{lista[i][j]:^5}]', end='')
    print('')

print('-=' * 30)
print(f'A soma dos valores pares é {sumPares}.')
print(f'A soma dos valores da terceira coluna é {sumCol3}.')
print(f'O maior valor da segunda linha é {max(lista[1])}.')
