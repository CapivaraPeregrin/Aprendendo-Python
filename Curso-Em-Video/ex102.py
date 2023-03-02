print(f'{" EXERCÍCIO 102 ":=^50}')

# Exercício Python 102: Crie um programa que tenha uma função fatorial()
# que receba dois parâmetros: o primeiro que indique o número a calcular
# e outro chamado show, que será um valor lógico (opcional) indicando se
# será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O numero a ser calculado
    :param show: (opicional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número num.
    """
    print('-' * 20)
    fat = 1
    txt = ''
    for c in range(num, 0, -1):
        fat *= c
        if show:
            simb = ' = ' if c == 1 else ' X '
            txt = txt + str(c) + simb
    txt = txt + str(fat)
    return txt


#Programa principal
help(fatorial)
print(fatorial(5, True))
