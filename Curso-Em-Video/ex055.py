print('{:=^40}'.format(' EXERCÍCIO 55 '))

# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

pesos = []

for i in range(1, 6):
    pesos.append(float(input(f'Peso da {i}º pessoa: ')))

maior = max(pesos)
menor = min(pesos)

print(f'O maior peso lido foi de {maior:.1f}Kg')
print(f'O menor peso lido foi de {menor:.1f}Kg')
