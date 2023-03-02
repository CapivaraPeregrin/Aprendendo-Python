print(f'{" EXERCÍCIO 81 ":=^50}')

# Exercício Python 081: Crie um programa que vai ler vários números
# e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numeros = []
while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)
    continuar = ' '
    while continuar not in 'SNY':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
