print(f'{" EXERCÍCIO 84 ":=^50}')

# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

grupo = []
pessoa = []
maiorPeso = 0
menorPeso = 0

while True:
    pessoa.append(input('Nome: ').strip())
    pessoa.append(float(input('Peso: ')))
    grupo.append(pessoa[:])

    if len(grupo) == 1:
        maiorPeso = pessoa[1]
        menorPeso = pessoa[1]
    else:
        if maiorPeso < pessoa[1]:
            maiorPeso = pessoa[1]
        if menorPeso > pessoa[1]:
            menorPeso = pessoa[1]

    pessoa.clear()

    continuar = ' '
    while continuar not in 'SNY':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(grupo)} pessoas.')
print(f'O maior peso foi de {maiorPeso:.1f}Kg. Peso de ', end='')
for c in grupo:
    if c[1] == maiorPeso:
        print(f'[{c[0]}] ', end='')
print(f'\nO menor peso foi de {menorPeso:.1f}Kg. Peso de ', end='')
for c in grupo:
    if c[1] == menorPeso:
        print(f'[{c[0]}] ', end='')
print('')
