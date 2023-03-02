print(f'{" EXERCÍCIO 77 ":=^50}')

# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais
# são as suas vogais.

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRÁTIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos: ', end='')
    for i in range(0, len(palavra)):
        if palavra[i] in 'AEIOUÁÀÃÂÉÍÌÊÕÓ':
            print(f'{palavra[i].lower()} ', end='')
