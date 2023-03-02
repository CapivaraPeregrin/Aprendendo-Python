from time import sleep

print(f'{" EXERCÍCIO 98 ":=^50}')

# Exercício Python 098: Faça um programa que tenha uma função chamada contador()
# , que receba três parâmetros: início, fim e passo. Seu programa tem que realizar
# três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada


def contador(ini, fim, passo):
    print('-=' * 25)
    print(f'Contagem de {ini} até {fim} de {abs(passo)} em {abs(passo)}')
    sleep(0.3)
    if ini > fim:
        passo = -1 * (abs(passo))
        fim -= 1
    else:
        passo = (abs(passo))
        fim += 1
    for c in range(ini, fim, passo):
        print(c, end=' ')
        sleep(0.3)
    print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 25)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
final = int(input('Fim: '))
passada = int(input('Passo: '))
contador(inicio, final, passada)
