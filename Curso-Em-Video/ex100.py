from random import randint
from time import sleep

print(f'{" EXERCÍCIO 100 ":=^50}')

# Exercício Python 100: Faça um programa que tenha uma lista chamada números
# e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear
# 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
# soma entre todos os valores pares sorteados pela função anterior.


def sorteia():
    print('Sorteando 5 valores da lista: ')
    lista = []
    for c in range(0, 5):
        lista.append(randint(0, 10))
        sleep(0.5)
        print(lista[c], end=' ')
    print('PRONTO!')
    return lista


def somapar(lista3):
    soma = 0
    for c in lista3:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista3}, temos {soma}')


lista2 = sorteia()
somapar(lista2)
