
# Aula 14 – Estrutura de repetição while
# Nessa aula 14, vamos continuar a estudar os laços e vamos aprender
# a usar a estrutura de repetição while no Python. Por exemplo:
# c=1
# while c !=10:
#   print(c)
#   c+=1
# print(‘Acabou’)


print('{:=^40}'.format(' EXERCÍCIO 57 '))


sexo = input('Informe seu sexo: [M/F] ').strip().upper()

while sexo not in 'MF':
    print('Dados Inválidos. ', end='')
    sexo = input('Por favor, informe seu sexo: ').strip().upper()
print(f'Sexo {sexo} registrado com sucesso')
