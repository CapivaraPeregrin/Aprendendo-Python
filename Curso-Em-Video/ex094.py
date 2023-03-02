print(f'{" EXERCÍCIO 94 ":=^50}')

# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias
# pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários
# em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoa = dict()
grupo = list()
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
    while pessoa['sexo'] not in 'FM':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())

    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
media = 0
female = ''
for v in grupo:
    media += v['idade']
    if v['sexo'] == 'F':
        female = v['nome'] if female == '' else female + ', ' + v['nome']
media = media / len(grupo)
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram {female}.')
print('D) Lista das pessoas que estão acima da média:')
for ind in grupo:
    if ind['idade'] > media:
        print('   ', end='')
        for k, c in ind.items():
            print(f'{k} = {c}; ', end='')
        print('')
print('<< ENCERRADO >>')
