from datetime import date

print(f'{" EXERCÍCIO 92 ":=^50}')

# Exercício Python 092: Crie um programa que leia nome, ano de nascimento
# e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se
# por acaso a CTPS for diferente de ZERO, o dicionário receberá também
# o ano de contratação e o salário. Calcule e acrescente, além da idade
# , com quantos anos a pessoa vai se aposentar.

pessoa = {}
pessoa['nome'] = input('Nome: ').strip()
idade = date.today().year - int(input('Ano de Nascimento: '))
pessoa['idade'] = idade
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] > 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = idade + 35 - (date.today().year - pessoa['contratação'])

print('-=' * 20)
for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')
