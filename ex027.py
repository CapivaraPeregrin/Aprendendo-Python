print('====== EXERCÍCIO 27 ======')

#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nomeCompleto = str(input('Digite o seu nome completo: ')).strip().split()
print('Seu primeiro nome é {}'.format(nomeCompleto[0]))
print('Seu último nome é {}'.format(nomeCompleto[-1]))
