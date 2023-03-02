from time import sleep

print(f'{" EXERCÍCIO 106 ":=^50}')

# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help
# do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando
# o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use
# cores.


def escreva(txt, cor):
    cor = str(cor).lower()
    if cor not in ['verde', 'azul', 'branco', 'vermelho']:
        print('ERRO, com indefinida')
    elif cor == 'verde':
        print('\033[1:42m', end='')
    elif cor == 'azul':
        print('\033[1:44m', end='')
    elif cor == 'branco':
        print('\033[1:7:40m', end='')
    elif cor == 'vermelho':
        print('\033[1:41m', end='')

    if cor != 'branco':
        tam = len(txt) + 4
        print('~' * tam)
        print(f'{txt:^{tam}}')
        print('~' * tam)
    else:
        print(help(func))
    print('\033[m', end='')


while True:
    escreva('SISTEMA DE AJUDA PyHELP', 'verde')
    func = input('Função ou Biblioteca > ').lower().strip()
    if func == 'fim':
        sleep(1)
        escreva('ATÉ LOGO!', 'vermelho')
        break
    escreva(f"Acessando o manual do comando '{func}'", 'azul')
    sleep(1)
    escreva(func, 'branco')
    sleep(1)
