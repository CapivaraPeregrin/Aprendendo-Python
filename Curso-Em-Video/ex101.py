from datetime import datetime

# def contador(i, f, p):
#     """
#     -> Faz uma contagem na tela
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: Sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end='..')
#         c += p
#     print('FIM')
#
#
# contador(0, 100, 10)

print(f'{" EXERCÍCIO 101 ":=^50}')

# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se
# uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    global idade
    idade = datetime.today().year - ano
    if idade > 70 or (idade < 18 and idade >= 16):
        return 'VOTO OPCIONAL'
    elif idade < 16:
        return 'NÃO VOTA'
    else:
        return 'VOTO OBRIGATÓRIO'

print('-' * 30)
anoNasc = int(input('Em que ano você nasceu? '))

if 0 > anoNasc or anoNasc > datetime.today().year:
    print('Ano inválido')
condicao = voto(anoNasc)
print(f'Com {idade} anos: {condicao}.')
