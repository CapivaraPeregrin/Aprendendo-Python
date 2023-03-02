import time

print(f'{" EXERCÍCIO 89 ":=^50}')

# Exercício Python 089: Crie um programa que leia nome e duas notas de vários
# alunos e guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

aluno = []
turma = []
media = 0
while True:
    aluno.append(input('Nome: '))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    turma.append(aluno[:])
    aluno.clear()
    continuar = ' '
    while continuar not in 'SNY':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print('No.', f'{"NOME":<15}', f'{"MÉDIA":^10}')
print('-' * 28)
for i in range(0, len(turma)):
    media = (turma[i][1] + turma[i][2])/2
    print(f'{i:<3}', f'{turma[i][0]:<15}', f'{media:^10.1f}')

while True:
    print('-' * 28)
    num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if num == 999:
        print('FINALIZANDO...')
        time.sleep(1)
        break
    print(f'Notas de {turma[num][0]} são {turma[num][1:]}')
print('<<< VOLTE SEMPRE >>>')
