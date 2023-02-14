print('====== EXERCÍCIO 06 ======')
# Programa que mostre o dobro o triplo
# e a raiz quadrada de um número

numero = int(input('Digite um número: '))

print('O dobro do número: {} \nO triplo do número: {}\nA raiz quadrada : {:.3f}'.format((numero*2), (numero*3), pow(numero, (1/2))))
