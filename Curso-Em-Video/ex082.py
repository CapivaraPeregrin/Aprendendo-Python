print(f'{" EXERCÍCIO 82 ":=^50}')

# Exercício Python 082: Crie um programa que vai ler vários números
# e colocar em uma lista. Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SNY':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

impar = []
par = []
for c in numeros:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

print('-=' * 30)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
