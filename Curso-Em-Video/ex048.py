print('{:=^40}'.format(' EXERCÍCIO 48 '))

# Exercício Python 48: Faça um programa que calcule a soma entre todos
# os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

qtde = 0
soma = 0

for i in range(0, 500, 3):
    if i % 2 != 0:
        soma += i
        qtde += 1

print(f'A soma de todos os {qtde} valores solicitados é {soma}.')
