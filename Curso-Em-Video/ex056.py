print('{:=^40}'.format(' EXERCÍCIO 56 '))

# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo
# de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

pessoa = []  # ['nome', 'idade', 'sexo']
todos = []
soma = 0
maisVelho = ['Não informado', 'Não informado']
jovensMulheres = 0
qtdeM = 0

for i in range(1, 5):
    print('----- {}º PESSOA -----')
    pessoa.append(input('Nome: '))
    pessoa.append(int(input('Idade: ')))
    pessoa.append(input('Sexo [M/F]: ').upper().strip())
    todos.append(pessoa)

    soma += pessoa[1]
    if pessoa[2] == 'F' and pessoa[1] < 20:
        jovensMulheres += 1
    elif pessoa[2] == 'M':
        qtdeM += 1
        if qtdeM == 1:
            maisVelho[0] = pessoa[0]
            maisVelho[1] = pessoa[1]
        if pessoa[1] > maisVelho[1]:
            maisVelho[0] = pessoa[0]
            maisVelho[1] = pessoa[1]

    pessoa.clear()

media = soma / len(todos)
print(f'A média de idade do grupo é de {media:.1f} anos.')
print(f'O homem mais velhos possui {maisVelho[1]} anos e se chama {maisVelho[0]}.')
print(f'Ao todo são {jovensMulheres} mulheres com menos de 20 anos.')
