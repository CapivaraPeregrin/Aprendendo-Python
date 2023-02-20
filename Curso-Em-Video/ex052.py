print('{:=^40}'.format(' EXERCÍCIO 52 '))

# Exercício Python 52: Faça um programa que leia um
# número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
eprimo = True
qtde = 0

for i in range(1, num+1):
    if num % i == 0:
        eprimo = False
        print(f'\033[33m{i}', end=' ')
        qtde += 1
    else:
        print(f'\033[31m{i}', end=' ')

if qtde == 2:
    eprimo = True

print('\033[m')
print(f'O número {num} foi divisível {qtde} vezes.')
print('E por isso ele ', end='')
if eprimo:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')
