print('====== EXERCÍCIO 40 ======')

# Exercício Python 040: Crie um programa que leia duas notas
# de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Insira a primeira nota do aluno: '))
nota2 = float(input('Insira a segunda nota do aluno: '))
media = (nota2 + nota1)/2

print(f'Tirando {nota1} e {nota2} a média do aluno foi : {media:.2f}')
print('O aluno está ', end='')
if media < 5:
    print('REPROVADO')
elif media >= 7:
    print('APROVADO')
else:
    print('em RECUPERAÇÃO')
