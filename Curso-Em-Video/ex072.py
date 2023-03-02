# # Anotação aula 16 Tuplas
# # [] lista
# # {} dicionario
# # () tupla ou só virgulas para python > 3.5
#
# # Tuplas são imutáveis
#
# lanche = ('hamburger', 'suco', 'pizza', 'pudim')
# print(lanche)
# print(lanche[1])
# print(lanche[1:3]) # o ultimo é desconsiderado
# print(lanche[1:])
# print(lanche[:2]) # o ultimo é desconsiderado
#
# # Tuplas são imutáveis
# # lanche[1] = 'Refri'
#
# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# for i in range(0, len(lanche)):
#     print(lanche[i])
#
# print('Comi pra caramba!')
#
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')

print(f'{" EXERCÍCIO 72 ":=^50}')

# Exercício Python 72: Crie um programa que tenha uma dupla totalmente
# preenchida com uma contagem por extenso, de zero até vinte. Seu programa
# deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um  número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {numeros[num]}')
        break
    else:
        print('Tente novamente. ', end='')
