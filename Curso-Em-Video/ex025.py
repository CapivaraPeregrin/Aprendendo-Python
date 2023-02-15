print('====== EXERCÍCIO 25 ======')

#Exercício Python 25: Crie um programa que leia o
# nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Qual é o seu nome completo? ')).upper().strip().split()
print('Seu nome tem Silva? {}'.format('SILVA' in nome))
