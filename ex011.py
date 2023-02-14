import math

print('====== EXERCÍCIO 11 ======')
#Exercício Python 11: Faça um programa que leia a largura
# e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo
# que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Informe a largura da parede em metros: '))
altura = float(input('Informe a altura da parede em metros: '))
area = altura * largura
litros = math.ceil(area / 2)

print(f'Será necessário {litros:n}L de tinta para pintar a parede')
