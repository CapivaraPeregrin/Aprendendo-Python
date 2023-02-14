import math

print('====== EXERCÍCIO 15 ======')
#Exercício Python 15: Escreva um programa que pergunte
# a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60
# por dia e R$0,15 por Km rodado.

kmPercorrido = float(input('Quantos Km rodados? '))
dias = math.ceil(float(input('Quantos dias alugados? ')))
total = (60 * dias) + (0.15 * kmPercorrido)
print(f'O total a pagar é de R${total:.2f}')
