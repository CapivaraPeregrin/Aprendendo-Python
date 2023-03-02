print(f'{" EXERCÍCIO 79 ":=^50}')

# Exercício Python 079: Crie um programa onde o usuário possa digitar vários
# valores numéricos e cadastre-os em uma lista. Caso o número já exista lá
# dentro, ele não será adicionado. No final, serão exibidos todos os
# valores únicos digitados, em ordem crescente.

numeros = []

while True:
    num = (int(input('Digite um valor: ')))
    if len(numeros) == 0:
        numeros.append(num)
    elif num in numeros:
        print('Valor duplicado! Não vou adicionar...')
    elif num < min(numeros):
        numeros.insert(0, num)
    elif num > max(numeros):
        numeros.append(num)

    continuar = ' '
    while continuar not in 'SsNn':
        continuar = input('Quer continuar: [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'Você digitou os valores {numeros}')
