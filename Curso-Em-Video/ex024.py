print('====== EXERCÍCIO 24 ======')

#Exercício Python 24: Crie um programa
# que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Em que cidade você nasceu? ')).strip().split()[0].upper()
print(cidade == 'SANTO')


