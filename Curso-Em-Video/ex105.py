print(f'{" EXERCÍCIO 105 ":=^50}')

# Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
#
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas(*num, sit=False):
    """
    ->Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opicional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """

    print('-' * 32)
    dicio = dict()
    dicio['tamanho'] = len(num)
    dicio['maior'] = max(list(num))
    dicio['menor'] = min(list(num))
    dicio['média'] = (sum(num)) / len(num)
    if sit:
        txt = 'BOA'
        if dicio['média'] < 7:
            txt = 'RAZOÁVEL'
        if dicio['média'] < 6:
            txt = 'RUIM'
        dicio['situação'] = txt
    return dicio


# Programa Principal
resp = notas(5.5, 2.5, 1.0, 6.5, sit=False)
print(resp)
help(notas)
