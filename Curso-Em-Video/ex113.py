print(f' EXERCÍCIO 113 '.center(30))

# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m', end='')
            print('ERRO: por favor, digite um número inteiro válido.')
            print('\033[m', end='')
            continue
        except (KeyboardInterrupt):
            print('\033[31m', end='')
            print('\nUsuário preferiu não digitar esse número.')
            print('\033[m', end='')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31m', end='')
            print('ERRO: por favor, digite um número real válido.')
            print('\033[m', end='')
            continue
        except (KeyboardInterrupt):
            print('\033[31m', end='')
            print('\nUsuário preferiu não digitar esse número.')
            print('\033[m', end='')
            return 0
        else:
            return n


print('-' * 30)
# Programa principal
n = leiaint('Digite um inteiro: ')
f = leiaFloat('Digite um real: ')
print(f'O valor digitado foi {n} e o real foi {f}')
