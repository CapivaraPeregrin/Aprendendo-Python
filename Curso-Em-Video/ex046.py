import time

# Anotação aula 13

for c in range(6, 1, -1):
    print(c)
print ('FIM')

print('{:=^40}'.format(' EXERCÍCIO 46 '))

# Exercício Python 46: Faça um programa que mostre na tela
# uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

for c in range(10, -1, -1):
    print(c, end='')
    if c == 0:
        print('.')
    else:
        time.sleep(1)
        print(', ', end='')
print('BUM! BUM! POOOW!')
