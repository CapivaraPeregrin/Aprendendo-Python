print('{:=^40}'.format(' EXERCÍCIO 51 '))

# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e
# a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 20)
p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(0, 10):
    print(p1, end=' \u2192 ') #Usando unicode seta
    p1 += razao
print('ACABOU!')
