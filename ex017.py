import math

print('====== EXERCÍCIO 17 ======')
#Exercício Python 17: Faça um programa que leia o comprimento
# do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

catop = float(input('Comprimento do cateto oposto: '))
catadj = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catop, catadj)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
