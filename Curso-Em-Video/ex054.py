from datetime import date

print('{:=^40}'.format(' EXERCÍCIO 54 '))

# Exercício Python 54: Crie um programa que leia o ano de nascimento
# de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.

anos = []
contMaior = 0
contMenor = 0

for i in range(0, 7):
    anos.append(int(input(f'Em que ano a {i+1}º pessoa nasceu? ')))


for i in anos:
    if i + 18 <= date.today().year:
        contMaior += 1
    else:
        contMenor += 1

print(f'Ao todo tivemos {contMaior} pessoas maiores de idade')
print(f'E tivemos {contMenor} pessoas menores de idade')
