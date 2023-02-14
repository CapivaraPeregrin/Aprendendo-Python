print('====== EXERCÍCIO 14 ======')
#Exercício Python 14: Escreva um programa que converta
# uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.

graus = float(input('Digite uma temperatura em ºC: '))
fahrenheit = (graus * 1.8) + 32
print(f'A temperatura de {graus:.1f}ºC corresponde a {fahrenheit:.1f}ºF!')
