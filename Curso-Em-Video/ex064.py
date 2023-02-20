print(f'{" EXERCÍCIO 64 ":=^50}')

# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de
# parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

qtde = soma = 0
numero = int(input('Digite um número [999 para parar]: ').strip())
while numero != 999:
    qtde += 1
    soma += numero
    numero = int(input('Digite um número [999 para parar]: ').strip())
print(f'Você digitou {qtde} números e a soma entre eles foi {soma}.')
