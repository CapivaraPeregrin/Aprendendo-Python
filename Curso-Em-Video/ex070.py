print(f'{" EXERCÍCIO 70 ":=^50}')

# Exercício Python 70: Crie um programa que leia o nome e o preço
# de vários produtos. O programa deverá perguntar se o usuário vai
# continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('-' * 50)
print(f'{"LOJA SUPER BARATÃO":^50}')
print('-' * 50)
total = pdtCaros = 0
maisBarato = ['', 0]
primeiraVez = True

while True:
    nome = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))

    total += preco
    if preco > 1000:
        pdtCaros += 1
    if primeiraVez:
        maisBarato = [nome, preco]
        primeiraVez = False
    elif maisBarato[1] > preco:
        maisBarato = [nome, preco]

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar: [S/N] ').strip()[0].upper()
    if resp == 'N':
        break

print(f'{" FIM DO PROGRAMA ":-^50}')
print(f'Total da compra foi de R${total:.2f}')
print(f'Temos {pdtCaros} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {maisBarato[0]} que custa R${maisBarato[1]:.2f}')
