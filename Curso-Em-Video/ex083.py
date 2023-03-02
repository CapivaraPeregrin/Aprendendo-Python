print(f'{" EXERCÍCIO 83 ":=^50}')

# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com
# os parênteses abertos e fechados na ordem correta.

exp = input('Digite a expressão: ')
contador = 0
for c in exp:
    if c == '(':
        contador += 1
    if c == ')':
        contador -= 1
    if contador < 0:
        break
if contador == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
