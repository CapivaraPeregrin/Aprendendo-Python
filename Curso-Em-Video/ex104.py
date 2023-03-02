print(f'{" EXERCÍCIO 104 ":=^50}')

# Exercício Python 104: Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)


def leiaint(txt):
    while True:
        if txt.isnumeric():
            break
        else:
            txt = input('Digite um número: ').strip()
            if not txt.isnumeric():
                print('\033[31m', end='')
                print('ERRO! Digite um número inteiro válido.')
                print('\033[m', end='')
    return int(txt)


print('-' * 20)

# Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
