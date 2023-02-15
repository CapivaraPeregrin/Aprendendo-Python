from math import radians, sin, tan, cos

print('====== EXERCÍCIO 18 ======')

#Exercício Python 18: Faça um programa que leia
# um ângulo qualquer e mostre na tela o valor do
# seno, cosseno e tangente desse ângulo.

angulo = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))
