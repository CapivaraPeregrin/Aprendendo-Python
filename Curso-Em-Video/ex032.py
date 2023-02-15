import datetime

print('====== EXERCÍCIO 32 ======')

# Exercício Python 32: Faça um programa que leia um ano qualquer
# e mostre se ele é bissexto.

ano = int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
data = str(ano) + '-12-31'
data = datetime.date.fromisoformat(data)

if datetime.date.timetuple(data)[7] == 366:
    print('O ano {} é BISSEXTO'.format(ano))
elif datetime.date.timetuple(data)[7] == 365:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
else:
    print('Erro')
