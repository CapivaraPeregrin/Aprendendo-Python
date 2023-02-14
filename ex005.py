print('====== EXERCÍCIO 05 ======')
#Exercício Python 5: Faça um programa que leia
# um número Inteiro e mostre na tela o seu sucessor
# e seu antecessor.

numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(numero, antecessor, sucessor))
