print('====== EXERCÍCIO 23 ======')

#Exercício Python 23: Faça um programa que leia um número
#de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = str(input('Informe um número: ')).strip()
print('Analisando o número {}'.format(num))
num = '0000' + num
print('Unidade {}'.format(num[len(num)-1]))
print('Dezena {}'.format(num[len(num)-2]))
print('Centena {}'.format(num[len(num)-3]))
print('Milhar {}'.format(num[len(num)-4]))


print('\n====== Forma matemática ======')

#outra forma
num = int(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
