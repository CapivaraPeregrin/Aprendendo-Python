print(f'{" EXERCÍCIO 75 ":=^50}')

# Exercício Python 075: Desenvolva um programa que leia quatro valores
# pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

pares = ''
txt = ('um', 'outro', 'mais um', 'o último')
valores = []
for i in range(0, 4):
    valores.append(int(input(f'Digite {txt[i]} número: ')))
    if valores[i] % 2 == 0:
        pares = pares + str(valores[i]) + ' '

tupla = tuple(valores)
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
print(f'Os valores pares digitados foram {pares}')
