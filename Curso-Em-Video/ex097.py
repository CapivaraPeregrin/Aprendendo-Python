print(f'{" EXERCÍCIO 97 ":=^50}')

# Exercício Python 097: Faça um programa que tenha uma função chamada escreva()
# , que receba um texto qualquer como parâmetro e mostre uma mensagem com
# tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~


def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'{txt:^{tam}}')
    print('~' * tam)


escreva('Teste')
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
