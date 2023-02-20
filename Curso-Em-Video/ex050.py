print('{:=^40}'.format(' EXERCÍCIO 50 '))

# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

numeros = [0, 0, 0, 0, 0, 0]
soma = 0
qtde = 0

for i in range(0, 6):
    numeros[i] = int(input(f'Insira o {1+i}º número: '))
    if numeros[i] % 2 == 0:
        soma += numeros[i]
        qtde += 1
print(f'A soma dos {qtde} números pares informados é {soma}')
