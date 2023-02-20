print(f'{" EXERCÍCIO 66 ":=^50}')

# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a
# condição de parada. No final, mostre quantos números foram digitados e qual
# foi a soma entre elas (desconsiderando o flag).

soma = qtde = 0
while True:
    numero = int(input('Digite um valor (999 para parar): ').strip())
    if numero == 999:
        break
    soma += numero
    qtde += 1
print(f'A soma dos {qtde} valores foi {soma}!')
