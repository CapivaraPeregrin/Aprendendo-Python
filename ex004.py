print('====== EXERCÍCIO 03 ======')
#Exercício Python 4: Faça um programa que leia algo
# pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

variavel = input('Digite algo: ')
print('O tio primitivo desse valor é {}'.format(type(variavel)))
print('Só tem espaços? {}'.format(variavel.isspace()))
print('É um número? {}'.format(variavel.isnumeric()))
print('É alfabético? {}'.format(variavel.isalpha()))
print('É alfanumérico? {}'.format(variavel.isalnum()))
print('Está em maiúsculas? {}'.format(variavel.isupper()))
print('Está em minúsculas? {}'.format(variavel.islower()))
print('Está capitalizada? {}'.format(variavel[0].isupper() and variavel[1:].islower()))
print('Está capitalizada? {}'.format(variavel.istitle()))
