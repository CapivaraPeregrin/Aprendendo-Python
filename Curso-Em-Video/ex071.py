print(f'{" EXERCÍCIO 71 ":=^50}')

# Exercício Python 071: Crie um programa que simule o funcionamento
# de um caixa eletrônico. No início, pergunte ao usuário qual será
# o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

print('\u2261' * 40)
print('{:^50}'.format('BANCO CEV'))
print('\u2261' * 40)

cedulaQtde = [0, 0, 0, 0]
cedulaValor = [50, 20, 10, 1]
valor = int(input('Qual valor você quer sacar? R$'))

for i in range(0, 4):
    cedulaQtde[i] = valor // cedulaValor[i]
    valor -= (cedulaQtde[i] * cedulaValor[i])
    if cedulaQtde[i] != 0:
        print(f'Total de {cedulaQtde[i]} cédulas de R${cedulaValor[i]} ')

print('\u2261' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
