print(f'{" EXERCÍCIO 76 ":=^50}')

# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes
# de produtos e seus respectivos preços, na sequência. No final, mostre uma
# listagem de preços, organizando os dados em forma tabular.

lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Tranferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livro', 34.9)

print('-' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-' * 50)
for c in range(0, len(lista), 2):
    print(f'{lista[c]:.<40}R${lista[c+1]:>7.2f} ')
print('-' * 50)
