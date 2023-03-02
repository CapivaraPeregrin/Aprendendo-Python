from random import randint

print(f'{" EXERCÍCIO 74 ":=^50}')

# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.

num = [0, 0, 0, 0, 0]
for i in range(5):
    num[i] = randint(1, 10)
numeros = tuple(num)

print(f'Os valores sorteados foram: ', end='')
for c in numeros:
    print(c, end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
