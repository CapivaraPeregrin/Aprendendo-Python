print('====== EXERCÍCIO 08 ======')
#Exercício Python 8: Escreva um programa que
# leia um valor em metros e o exiba convertido
# em centímetros e milímetros.

metro = float(input('Digite um valor em metros: '))
print('O valor corresponde a {:.0f}cm \nE a {:.0f}mm'.format(metro*100, metro*1000))
