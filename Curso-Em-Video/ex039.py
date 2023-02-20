import datetime

print('====== EXERCÍCIO 39 ======')

# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço
# militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input('Ano de nascimento: '))
anoAlistamento = ano + 18
anoAtual = datetime.date.today().year

if anoAlistamento < anoAtual:
    print(f'O ano para seu alistamento foi à {anoAtual-anoAlistamento} ano(s) atrás! em {anoAlistamento}.')
elif anoAlistamento > anoAtual:
    print(f'O ano para seu alistamento será daqui a {anoAlistamento - anoAtual} ano(s)! em {anoAlistamento}.')
else:
    print('Seu alistamento é neste ano {}.'.format(anoAtual))
