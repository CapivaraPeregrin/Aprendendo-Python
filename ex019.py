import random

print('====== EXERCÍCIO 19 ======')
#Exercício Python 19: Um professor quer sortear um
# dos seus quatro alunos para apagar o quadro. Faça
# um programa que ajude ele, lendo o nome dos alunos e
# escrevendo na tela o nome do escolhido.

alun1 = input('Primeiro aluno: ')
alun2 = input('Segundo aluno: ')
alun3 = input('Terceiro aluno: ')
alun4 = input('Quarto aluno: ')

lista = [alun1, alun2, alun3, alun4]
num = random.randint(0, 3)
print('O aluno escolhido foi {}'.format(lista[num]))
