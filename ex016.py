from math import floor, sqrt, trunc

num = 7
raiz = sqrt(num)
print('a raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

print('====== EXERCÍCIO 16 ======')
#Exercício Python 16: Crie um programa que leia um número Real
# qualquer pelo teclado e mostre na tela a sua porção Inteira.

numero = float(input('Digite um valor: '))
print('O valor digitado é {} e sua porção inteira é {}'.format(numero, trunc(numero)))
