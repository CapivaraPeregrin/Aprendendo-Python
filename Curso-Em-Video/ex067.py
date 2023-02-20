print(f'{" EXERCÍCIO 67 ":=^50}')

# Exercício Python 67: Faça um programa que mostre a tabuada de vários
# , um de cada vez, para cada valor digitado pelo usuário. O programa
# será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if num < 0:
        break
    for i in range(1, 11):
        produto = num * i
        print(f'{num} x {i} = {produto}')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
