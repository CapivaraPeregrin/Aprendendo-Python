print('====== EXERCÍCIO 37 ======')

# Exercício Python 37: Escreva um programa em Python
# que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão: 1
# para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão:')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')

opcoes = {1: 'BINÁRIO', 2: 'OCTAL', 3: 'HEXADECIMAL'}
escolha = int(input('Sua opção: '))

convertido = ''
if escolha == 1:
    convertido = str(bin(num))[2:]
elif escolha == 2:
    convertido = str(oct(num))[2:]
elif escolha == 3:
    convertido = str(hex(num))[2:]
else:
    print('Opção inválida!')

print(f'{num} convertido para {opcoes[escolha]} é igual a {convertido}')
