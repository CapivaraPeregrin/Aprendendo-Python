print(f'{" EXERCÍCIO 65 ":=^50}')

# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o
# menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

qtde = soma = maior = menor = 0
continuar = 'S'
lista = []

while continuar == 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    qtde += 1
    lista.append(numero)

    continuar = input('Quer continuar? [S/N] ').strip()[0].upper()
    while continuar not in 'SN':
        print('Valor inválido')
        continuar = input('Quer continuar? [S/N] ').strip()[0].upper()

maior = max(lista)
menor = min(lista)
print(f'Você digitou {qtde} números e a média foi {soma / qtde:.2f}')
print(f'O maior valor foi {maior} e o menor valor {menor}')
