print('{:=^40}'.format(' EXERCÍCIO 49 '))

# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada
# de um número que o usuário escolher, só que agora utilizando um laço for.

numero = float(input('Digite um número: '))

print('Tabuada: \n')
for i in range(1, 11):
    print('{} X {} = {:.2f}'.format(numero, i, numero*i))
