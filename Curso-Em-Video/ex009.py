print('====== EXERCÍCIO 09 ======')
#Exercício Python 9: Faça um programa que leia um
# número Inteiro qualquer e mostre na tela a sua tabuada.

numero = float(input('Digite um número: '))

print('Tabuada: \n')
for i in range(1, 11):
    print('{} X {} = {:.2f}'.format(numero, i, numero*i))
