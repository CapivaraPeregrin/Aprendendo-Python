# #Anotação aula 17 Listas
#
# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 0)
# num.pop(2)
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')
#
# a = [1, 2, 3]
# b = a[:] #copia dos dados
# b = a # Ligação referencia

print(f'{" EXERCÍCIO 78 ":=^50}')

# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os
# em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as
# suas respectivas posições na lista.

numeros = list()
for i in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a Posição {i}: ')))

print('=-' * 30)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {max(numeros)} nas posições ', end='')
for i in range(0, 5):
    if numeros[i] == max(numeros):
        print(i, end='... ')
print(f'\nO menor valor digitado foi {min(numeros)} nas posições ', end='')
for i in range(0, 5):
    if numeros[i] == min(numeros):
        print(i, end='... ')
