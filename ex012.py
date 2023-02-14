print('====== EXERCÍCIO 12 ======')
#Exercício Python 12: Faça um algoritmo
# que leia o preço de um produto e mostre
# seu novo preço, com 5% de desconto.

preco = float(input('Digite um valor: '))
novopreco = preco*0.95
print(f'O preço do produto com desconto de 5% é R${novopreco:.2f}')