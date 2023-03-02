print(f'{" EXERCÍCIO 90 ":=^50}')

# Exercício Python 090: Faça um programa que leia nome e média de um aluno
# , guardando também a situação em um dicionário. No final, mostre o
# conteúdo da estrutura na tela.

aluno = {}

aluno['nome'] = input('Nome: ')
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print('-=' * 20)

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f' - {k} é igual a {v}')

# print(f'- O nome é igual a {aluno["nome"]}')
# print(f'- A média é igual a {aluno["média"]}')
# print(f'- A situação é igual a {aluno["situação"]}')
