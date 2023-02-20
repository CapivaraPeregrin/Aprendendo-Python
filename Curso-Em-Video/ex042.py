import math

print('====== EXERCÍCIO 42 ======')

# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando
# o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

lado1 = float(input('Primeiro segmento: '))
lado2 = float(input('Segundo segmento: '))
lado3 = float(input('Terceiro segmento: '))

lados = [lado3, lado2, lado1]

maior = max(lados)
menor = min(lados)
medio = sum([lado3, lado2, lado1]) - maior - menor

if maior < sum([lado3, lado2, lado1]) - maior:
    print('Os segmentos podem formar um triângulo ', end='')
    if lado3 == lado2 == lado1:
        print('EQUILÁTERO')
    elif lado3 == lado2 or lado3 == lado1 or lado2 == lado1:
        print('ISÓCELES', end='')
        if maior == math.sqrt(math.pow(menor, 2) + math.pow(medio, 2)):
            print(' e RETÂNGULO')
    elif maior == math.sqrt(math.pow(menor, 2) + math.pow(medio, 2)):
        print('RETÂNGULO')
    else:
        print('ESCALENO')
else:
    print('Os segmentos NÃO podem formar um triângulo!')
