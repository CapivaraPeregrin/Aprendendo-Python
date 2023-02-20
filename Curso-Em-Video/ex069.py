print(f'{" EXERCÍCIO 69 ":=^50}')

# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias
# pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

deMaior = mens = womens = 0

while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip()[0].upper()
    print('-' * 25)

    if idade > 18:
        deMaior += 1
    if idade < 20 and sexo == 'F':
        womens += 1
    if sexo == 'M':
        mens += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip()[0].upper()
    if continuar == 'N':
         break

print(f'Total de pessoas com mais de 18 anos: {deMaior}')
print(f'Ao todo temos {mens} homens cadastrados.')
print(f'E temos {womens} mulheres com menos de 20 anos.')
