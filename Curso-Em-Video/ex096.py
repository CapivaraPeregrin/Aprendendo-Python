print(f'{" EXERCÍCIO 96 ":=^50}')

# Exercício Python 096: Faça um programa que tenha uma função chamada
# área(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:.1f}X{comp:.1f} é de {a:.1f}m²')


print('Controle de Terrenos')
print('--------------------')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
