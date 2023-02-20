from random import randint

print(f'{" EXERCÍCIO 68 ":=^50}')

# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de
# vitórias consecutivas que ele conquistou no final do jogo.

print('=-' * 25)
print('VAMOS JOGAR PAR OU ÍMPAR')
vitorias = 0

while True:
    print('=-' * 25)
    userNum = int(input('Diga um valor: '))
    palpite = input('Par ou Ímpar? [P/I] ').strip()[0].upper()

    computNum = randint(0, 10)
    somaTexto = 'DEU ÍMPAR'    # impar por padrão
    resposta = 'IÍ'            # impar por padrão
    if (userNum + computNum) % 2:
        resposta = 'P'
        somaTexto = 'DEU PAR'

    print('-' * 50)
    print(f'Você jogou {userNum} e o computador {computNum}. ', end='')
    print(f'Total de {computNum + userNum} {somaTexto}')
    print('-' * 50)

    if palpite not in resposta:
        print('Você PERDEU!')
        print('=-' * 25)
        print(f'GAME OVER! Você venceu {vitorias} vezes.')
        break
    else:
        print('Você VENCEU!\nVamos jogar novamente... ')
        vitorias += 1
