print('====== EXERCÍCIO 33 ======')

#Exercício Python 33: Faça um programa que leia três números e mostre
# qual é o maior e qual é o menor.


n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
valores = [n1, n2, n3]

print('O menor valor digitado foi {}'.format(min(valores)))
print('O maior valor digitado foi {}'.format(max(valores)))
